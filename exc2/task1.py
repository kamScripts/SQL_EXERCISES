import sqlite3 as db



try:
    connection = db.connect("ShopDB.db")
    print("Connected to the database")
#sqlite.Error is a parent class for SQL related exception, therefore it catches all subclasses of that error.
except db.Error as e:
    print(f"Cannot connect: {e}")
else:
    cursor = connection.cursor()
    with open('schema.sql') as schema:
        sql_script=schema.read()
    cursor.executescript(sql_script)
    connection.commit()
    connection.close()
