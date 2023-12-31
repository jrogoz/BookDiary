from DB_access.modify_db import exec_query


def select_from_table(table_name, num=1, condition: str = None, order_by: str = None, group_by: str = None, *args):
    if args:
        cols = ", ".join([item for item in args])
    else:
        cols = "*"

    query = f"SELECT {cols} FROM {table_name}"

    if condition:
        query += " WHERE "
        query += condition

    if order_by:
        query += " ORDER BY "
        query += order_by

    if group_by:
        query += " GROUP BY "

    return exec_query(query, num)


