import unittest
from DB_access.select import select_from_table


class TestSelect(unittest.TestCase):

    def test_select_one_from_table(self):
        select_results = select_from_table('books', num=1)
        self.assertEqual(1, len(select_results))

    def test_select_many_from_table(self):
        select_results = select_from_table('books', num=3)
        self.assertEqual(3, len(select_results))

    def test_select_more_records_than_exists(self):
        select_results = select_from_table('books', num=20)
        self.assertGreater(20, len(select_results))

    def test_select_all_records_from_table(self):
        select_result = select_from_table('books')
        self.assertNotEqual(None, select_result)

    def test_select_where_id_equal_and_id_exists(self):
        select_result = select_from_table('books', condition='book_id = 3')
        self.assertEqual(1, len(select_result))

    def test_select_where_id_and_id_does_NOT_exist(self):
        select_result = select_from_table('books', condition='book_id = 300')
        self.assertEqual([], select_result)

    def test_select_where_id_greater_and_id_exists(self):
        select_result = select_from_table('books', condition='book_id > 2')
        self.assertLess(2, select_result[0][0])

    def test_select_where_id_lower_and_id_exists(self):
        select_result = select_from_table('books', condition='book_id < 4')
        self.assertGreater(4, select_result[-1][0])

    def test_select_where_id_between_and_id_exists(self):
        select_result = select_from_table('books', condition='book_id > 3 and book_id < 10')
        self.assertGreater(10, select_result[-1][0])
        self.assertLess(3, select_result[0][0])

    def test_select_from_table_order_by_id_asc(self):
        select_result = select_from_table('books', order_by='book_id', num=5)

        for i in range(len(select_result[:-1])):
            self.assertLess(select_result[i][0], select_result[i+1][0])

    def test_select_from_table_order_by_id_dsc(self):
        select_result = select_from_table('books', order_by='book_id desc')

        for i in range(len(select_result[:-1])):
            self.assertGreater(select_result[i][0], select_result[i + 1][0])

    def test_select_from_table_group_by(self):
        cols = ['status_id', 'COUNT(book_id) AS book_count']
        select_result = select_from_table('book_status', col_names=cols, group_by='status_id')
        self.assertGreaterEqual(4, len(select_result))


if __name__ == '__main__':
    unittest.main()
