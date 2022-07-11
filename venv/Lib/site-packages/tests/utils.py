import os

import pytest
from sqlalchemy import Column, Integer, MetaData, Table, Text

from flask_sqlalchemy_core import FlaskSQLAlchemy

DATABASE_URL = os.environ['DATABASE_URL']

db = FlaskSQLAlchemy(DATABASE_URL)

metadata = MetaData()


NotesTable = Table(
    'notes', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', Text, unique=True, nullable=False),
    Column('text', Text),
    sqlite_autoincrement=True,
)


NESTED_TRANSACTION_BACKENDS = {
    'postgres',
    'postgresql',
}


def backend_supports_transactions(db_url):
    dbtype = db_url.split('://')[0]
    return dbtype in NESTED_TRANSACTION_BACKENDS


require_nested_transactions = pytest.mark.skipif(
    not backend_supports_transactions(DATABASE_URL),
    reason="Backend doesn't support nested transactions.")
