import sqlite3
import csv
from decide_type import decide

def import_from_csv(file_name, db_name, table_name):
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()

        with open(file_name, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)

            # Extract column names from the first row
            column_names = next(csv_reader)
            columns = ', '.join(f'"{col}" {decide(col)}' for col in column_names)

            # Create table with dynamic column names
            # If primary key required add at the end of create query.
            create_table_query = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns});'
            cursor.execute(create_table_query)

            # Prepare insert query with placeholders
            placeholders = ', '.join('?' for _ in column_names)

            insert_query = f'INSERT INTO "{table_name}" VALUES ({placeholders});'

            # Insert rows from CSV
            for row in csv_reader:
                cursor.execute(insert_query, (row))
                
        connection.commit()

