import unittest
import os
import sqlite3
from db_handler import Db_handler

class TestDatabaseHandler(unittest.TestCase):
    DB_PATH = "test_sq_db.db"
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        
    def setUp(self):
        """Runs before each test, ensures a fresh connection."""
        self.db_handler = Db_handler(self.DB_PATH)
        
    def test_creation(self):
        """Test creation of the database."""
        self.db_handler.create_db()
        self.assertTrue(os.path.exists(self.DB_PATH))
        
    def test_table_creation(self):
        """Test the creation of the table"""
        test_query = """CREATE TABLE 'testing' (
            't' TEXT,
            'num' INTEGER
            );"""
        self.db_handler.create_table(test_query)
        self.assertTrue(self.db_handler.if_table_exists('testing'), "Table 'testing' not found")


if __name__ == "__main__":
    # verbosity attr generates more detailed output.
    unittest.main(verbosity=2)