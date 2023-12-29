from DB_access.connection import connect, disconnect

if __name__ == "__main__":
    conn, cur = connect()
    disconnect(conn, cur)

