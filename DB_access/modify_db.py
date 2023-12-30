import psycopg2
from DB_access.connection import connect, disconnect


def database_query(query, select: int = None):
    conn = None
    cur = None
    result = None

    try:
        conn, cur = connect()
        cur.execute(query)
        if select:
            result = cur.fetchmany(select)

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            disconnect(conn, cur)
        return result


def create_new_table(table_name, **kwargs):
    cols = ", ".join(["{} {}".format(k, v) for (k, v) in kwargs.items()])
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({cols});"
    database_query(query)


def insert_into_table(table_name, **kwargs):
    cols = ", ".join([k for k, _ in kwargs.items()])
    vals = ", ".join([v for _, v in kwargs.items()])
    query = f"INSERT INTO {table_name} ({cols}) VALUES ({vals});"
    database_query(query)


def update_table(table_name, condition: str = None, **kwargs):
    cols_vals = ", ".join(["{} = {}".format(k, v) for (k, v) in kwargs.items()])
    query = f"UPDATE {table_name} SET {cols_vals} where {condition};"
    database_query(query)


def select_from_table(table_name, num=1, *args):
    cols = ", ".join([item for item in args])
    if not args:
        cols = "*"
    query = f"SELECT {cols} FROM {table_name}"
    print(database_query(query, num))

