create_table_sales ="""CREATE TABLE IF NOT EXISTS sales_data (
    "Region" TEXT,
    "Country" TEXT,
    "Item Type" TEXT,
    "Sales Channel" TEXT,
    "Order Priority" TEXT,
    "Order Date" TEXT,
    "Order ID" INTEGER,
    "Ship Date" TEXT,
    "Units Sold" INTEGER,
    "Unit Price" REAL,
    "Unit Cost" REAL,
    "Total Revenue" REAL,
    "Total Cost" REAL,
    "Total Profit" REAL
);"""

select_montenegro = 'SELECT * FROM table WHERE Country=?;'

select_online_sales = 'SELECT * FROM table WHERE "Sales Chanel"=?;'

select = """SELECT Region, "Unit Price" FROM sales
                      WHERE "Unit Price">=?
                      ORDER BY  "Unit Price" DESC;"""