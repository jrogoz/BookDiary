import unittest
from config import config


class TestConfig(unittest.TestCase):
    def test_config_correct_arguments(self):
        expected_db = {
            'host': 'localhost',
            'port': '5433',
            'database': 'TestBookDiaryDB',
            'user': 'postgres',
            'password': '1234'
        }
        db = config(filename='database.ini')
        self.assertDictEqual(expected_db, db)

    def test_config_incorrect_filename(self):
        with self.assertRaises(OSError):
            config(filename='test.ini')

    def test_config_incorrect_section(self):
        with self.assertRaises(Exception):
            config(section='notpostgresql')


if __name__ == '__main__':
    unittest.main()