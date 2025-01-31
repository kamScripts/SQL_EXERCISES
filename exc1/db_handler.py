import sqlite3

class Db_handler:
    
    def __init__(self, db_name):
      self._db_name = db_name

      
    @property
    def db_name(self) -> str:
        """Getter for Database name (read-only)"""
        return self._db_name
    
    def create_db(self) -> None:
        """Create the database"""
        connection = sqlite3.connect(self.db_name)
        print(f'{self.db_name} created successfully.')
        connection.close()

    def create_table(self, query: str) -> None:
        """Create the table"""
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
    def if_table_exists(self, table_name: str) -> bool:
        """Check if a table exists in the SQLite database."""
        # sqlite_master is a table that contains records of all tables inside the database.
        # including type, name,, tbl_name, rootpage, and sql.
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?;"

        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            result = cursor.execute(query, (table_name,)).fetchone()
        # if table exists fetchone() returns tuple with table name, otherwise returns NoneType.
        return result is not None

