import psycopg2
from DB_access.connection import connect, disconnect


def exec_query(query, fetch_num: int = None):
    conn = None
    cur = None
    result = None
    select = True if 'select' in (query.lower()).split(' ') else False

    try:
        conn, cur = connect()
        cur.execute(query)
        if select:
            if fetch_num:
                result = cur.fetchmany(fetch_num)
            else:
                result = cur.fetchall()
        else:
            conn.commit()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            disconnect(conn, cur)
        return result
    

def create_new_table(table_name, **kwargs):
    cols = ", ".join(["{} {}".format(k, v) for (k, v) in kwargs.items()])
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({cols});"
    exec_query(query)


def insert_into_table(table_name, **kwargs):
    cols = ", ".join([k for k, _ in kwargs.items()])
    vals = ", ".join([v for _, v in kwargs.items()])
    query = f"INSERT INTO {table_name} ({cols}) VALUES ({vals});"
    exec_query(query)


def update_table(table_name, condition: str = None, **kwargs):
    cols_vals = ", ".join(["{} = {}".format(k, v) for (k, v) in kwargs.items()])
    query = f"UPDATE {table_name} SET {cols_vals} where {condition};"
    exec_query(query)




