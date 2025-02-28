CREATE TABLE Suppliers (
  supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
  supplier_name TEXT UNIQUE NOT NULL,
  contact_person TEXT,
  phone_number TEXT,
  email TEXT,
  address TEXT
);

CREATE TABLE Products (
  product_id INTEGER PRIMARY KEY AUTOINCREMENT,
  barcode TEXT UNIQUE,
  name TEXT NOT NULL UNIQUE,
  brand TEXT,
  cost_price REAL,
  supplier_id INTEGER,
  price REAL,
  FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Sales (
  sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_id INTEGER,
  sale_date NUMERIC DEFAULT CURRENT_TIMESTAMP,
  quantity INTEGER,
  payment_type TEXT,
  total_price REAL,
  FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  sale_id INTEGER,
  location TEXT,
  order_date NUMERIC DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (sale_id) REFERENCES Sales(sale_id),
  FOREIGN KEY (location) REFERENCES Stock(location)
);

CREATE TABLE Stock (
  stock_id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_id INTEGER,
  quantity INTEGER,
  location TEXT,
  FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
