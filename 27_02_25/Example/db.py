#Import SQLite
import sqlite3

#Create the connection
connection = sqlite3.connect("myShopDB.db")

print("Connected to DB!")

#We need a cursor
cursor = connection.cursor()


#Execute the select statement that will retrieve name, price and stock quantity
results = cursor.execute("SELECT name, price, QtyInStock FROM STOCK where price>19.99")

#Get a list of column names first
col_name_list = []
for tuple in results.description:
    col_name_list.append(tuple[0])

#Get the results of the statements in an array of tuples
results = results.fetchall()

print(col_name_list)

#Print each row of information 
for result in results:
    print(result)



connection.close()
print("Connection closed")

