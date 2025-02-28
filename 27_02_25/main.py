import sqlite3
from import_from_csv import import_from_csv

db_name = 'global_sales2.db'
data_file = 'sales.csv'

import_from_csv(data_file, db_name, 'sales')

with sqlite3.connect(db_name) as connection:
    cursor = connection.cursor()
    
    select_query = """SELECT "Item Type", "Sales Channel" FROM sales WHERE "Sales Channel" = ?
                   """
    
    cursor.execute(select_query, ("Offline", ))
    
    all_records = cursor.fetchall()
    
    for record in all_records:
        print(record)
    

