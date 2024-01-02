import unittest
import psycopg2
from DB_access.connection import connect, disconnect


class TestConnection(unittest.TestCase):
    def test_connect_OK(self):
        conn, cur = connect()
        self.assertNotEqual(None, conn)
        self.assertNotEqual(None, cur)

    def test_disconnect_OK(self):
        result = disconnect(*connect())
        self.assertEqual(None, result)

    def test_disconnect_cursor_is_none(self):
        conn, _ = connect()
        disconnect(conn, None)
        self.assertRaises(psycopg2.DatabaseError)

    def test_disconnect_conn_is_none(self):
        _, cur = connect()
        disconnect(None, cur)
        self.assertRaises(psycopg2.DatabaseError)

    def test_disconnect_conn_and_cursor_are_none(self):
        disconnect(None, None)
        self.assertRaises(psycopg2.DatabaseError)