import logging
from contextlib import contextmanager

from sqlalchemy import create_engine

from werkzeug.local import Local, get_ident, release_local

logger = logging.getLogger(__name__)


class FlaskSQLAlchemy:

    def __init__(self, database_url, **options):
        self._local = Local()
        self._database_url = database_url
        self._options = options
        self._engine = self.create_engine()

    def get_engine(self):
        return self._engine

    def create_engine(self):
        return create_engine(self._database_url, **self._options)

    def connect(self):
        try:
            self._local.connection
        except AttributeError:
            return self._new_connection_context()
        return self._reuse_connection_context()

    @contextmanager
    def _new_connection_context(self):
        logger.debug('[%s] Getting new connection from pool', get_ident())
        conn = self._engine.connect()
        self._local.connection = conn
        yield conn
        logger.debug('[%s] Releasing connection to pool', get_ident())
        self._local.connection = None
        release_local(self._local)
        conn.close()

    @contextmanager
    def _reuse_connection_context(self):
        logger.debug('[%s] Reusing connection', get_ident())
        yield self._local.connection
        logger.debug('[%s] Finished using connection', get_ident())

    @contextmanager
    def transaction(self, autocommit=True, rollback=False):
        with self.connect() as conn:
            logger.debug('[%s] Starting transaction', get_ident())
            trans = conn.begin_nested()
            try:

                # Yield the connection object, as it is
                # needed for actually running queries.
                # The transaction will be automatically committed upon
                # success, or rolled back if an exception is raised.
                yield conn

                if autocommit:
                    logger.debug('[%s] Committing transaction', get_ident())
                    trans.commit()

                if rollback:
                    logger.debug('[%s] Rolling back transaction', get_ident())
                    trans.rollback()

            except Exception:
                logger.debug('[%s] Rolling back transaction (exception)',
                             get_ident())
                trans.rollback()
                raise

    def execute(self, *args, **kwargs):
        with self.connect() as conn:
            return conn.execute(*args, **kwargs)
