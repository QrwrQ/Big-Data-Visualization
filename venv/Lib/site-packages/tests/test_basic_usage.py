from tests.utils import NotesTable, require_nested_transactions
from sqlalchemy import insert, select, func


def test_can_connect_to_database(db):
    pass


def test_can_write_object_to_database(db):

    query = insert(NotesTable).values(
        name='Hello',
        text='Hello world!')

    with db.connect() as conn:
        result = conn.execute(query)

    post_id, = result.inserted_primary_key
    assert post_id is not None


def test_database_is_emptied_between_test_runs(db):
    assert _count_rows(db, NotesTable) == 0


def test_transaction_rolls_back_on_exception(db):
    try:
        with db.transaction() as conn:
            conn.execute(insert(NotesTable).values(name='A'))
            raise ValueError
    except ValueError:
        pass

    assert _count_rows(db, NotesTable) == 0


@require_nested_transactions
def test_partial_transaction_commit(db):
    with db.transaction() as conn:
        conn.execute(insert(NotesTable).values(name='A'))

        try:
            with db.transaction() as conn:
                conn.execute(insert(NotesTable).values(name='B'))
                raise ValueError
        except ValueError:
            pass

        with db.transaction() as conn:
            conn.execute(insert(NotesTable).values(name='C'))

        conn.execute(insert(NotesTable).values(name='D'))

    rows = _get_all_rows(db, NotesTable)
    assert len(rows) == 3
    assert set(x.name for x in rows) == {'A', 'C', 'D'}


def _count_rows(db, table):
    query = select([func.count(table.c.id)])
    with db.connect() as conn:
        result = conn.execute(query)
        return result.scalar()


def _get_all_rows(db, table):
    query = select([table])
    with db.connect() as conn:
        result = conn.execute(query)
        return list(result)


@require_nested_transactions
class TestOneTransaction:

    def test_insert_data_in_transaction(self, db):
        query = insert(NotesTable).values(name='A', text='A')
        with db.transaction() as conn:
            conn.execute(query)

    def test_db_was_emptied(self, db):
        assert _count_rows(db, NotesTable) == 0


@require_nested_transactions
class TestNestedTransactions:

    def test_insert_data_in_transaction(self, db):
        query = insert(NotesTable).values(name='A', text='A')
        query1 = insert(NotesTable).values(name='B', text='B')
        with db.transaction() as conn:
            with db.transaction() as conn1:
                assert conn is conn1
                conn.execute(query)
            conn.execute(query1)

    def test_db_was_emptied(self, db):
        assert _count_rows(db, NotesTable) == 0


@require_nested_transactions
class TestNestedTransactionsWithRollback:

    def test_insert_data_in_transaction(self, db):
        query = insert(NotesTable).values(name='A', text='A')
        query1 = insert(NotesTable).values(name='B', text='B')

        with db.transaction() as conn:

            try:
                with db.transaction() as conn1:
                    assert conn is conn1
                    conn.execute(query)
                    raise ValueError()  # Just roll back!
            except ValueError:
                pass  # Ignore the exception above

            conn.execute(query1)

        assert _count_rows(db, NotesTable) == 1

    def test_db_was_emptied(self, db):
        assert _count_rows(db, NotesTable) == 0


@require_nested_transactions
def test_exception_in_outer_transaction(db):

    try:

        with db.transaction() as conn:

            with db.transaction():
                conn.execute(insert(NotesTable).values(name='A'))

            with db.transaction():
                conn.execute(insert(NotesTable).values(name='B'))

            raise ValueError

    except ValueError:
        pass

    assert _count_rows(db, NotesTable) == 0
