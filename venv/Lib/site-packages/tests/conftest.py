import logging

import pytest

from .utils import db as _database
from .utils import metadata

try:
    from nicelog import setup_logging
except ImportError:
    pass
else:
    setup_logging()

logging.getLogger().setLevel(logging.DEBUG)


@pytest.fixture(scope='function')
def db(db_schema):
    with _database.transaction(autocommit=False, rollback=True):
        # By wrapping execution in a transaction that automatically
        # gets rolled back, we can avoid having to recreate the whole
        # schema for every test function run.
        yield _database


@pytest.fixture(scope='session')
def db_schema():
    engine = _database.get_engine()

    # Clean up, in case tables were left around from a previous run.
    # This can happen if the test process was abruptly killed.
    metadata.drop_all(engine)

    metadata.create_all(engine)

    yield

    metadata.drop_all(engine)
