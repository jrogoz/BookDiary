def create_new_table(conn, cur, table_name, **kwargs):

    cols = ", ".join(["{} {}".format(k, v) for (k, v) in kwargs.items()])

    cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({cols});")
    conn.commit()


def insert_into_table(conn, cur, table_name, **kwargs):

    cols = ", ".join([k for k, _ in kwargs.items()])
    vals = ", ".join([v for _, v in kwargs.items()])

    cur.execute(f"INSERT INTO {table_name} ({cols}) VALUES ({vals})")
    conn.commit()

