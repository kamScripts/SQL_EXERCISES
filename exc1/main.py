from db_handler import Db_handler
import sqlite3

db_path = "MyShopDB.db"
db_handler = Db_handler(db_path)

my_query = """CREATE TABLE IF NOT EXISTS 'products' (    
    'product ID' INT PRIMARY KEY,
    'brand' TEXT,
    'name' TEXT,
    'price' REAL,
    'cost price' REAL,
    'quantity' INT,
    'last sale date' NUM
    );"""

db_handler.create_table(my_query)


