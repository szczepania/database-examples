import sqlite3
import pandas as pd
import random
from faker import Faker

fake = Faker()

db = sqlite3.connect('databases/sales_data_with_customers.db')
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        customer_id INTEGER,
        quantity_sold INTEGER,
        price REAL,
        date TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT,
        email TEXT
    )
''')

cursor.execute('DELETE FROM sales')

sample_sales_data = [
    (
        i + 1,
        random.randint(1, 100),  # Product ID
        random.randint(1, 50),  # Customer ID
        random.randint(1, 20),  # Quantity Sold
        round(random.uniform(10, 100), 2),  # Price
        fake.date_between(start_date='-30d', end_date='today').strftime('%Y-%m-%d')  # Date
    )
    for i in range(100)
]

cursor.executemany(
    'INSERT INTO sales (sale_id, product_id, customer_id, quantity_sold, price, date) VALUES (?, ?, ?, ?, ?, ?)',
    sample_sales_data)

db.commit()

cursor.execute('DELETE FROM customers')

sample_customers_data = [
    (
        i + 1,
        fake.name(),
        fake.email()
    )
    for i in range(50)
]

cursor.executemany('INSERT INTO customers (customer_id, customer_name, email) VALUES (?, ?, ?)', sample_customers_data)
db.commit()

query = '''
    SELECT
        s.sale_id,
        s.product_id,
        s.customer_id,
        s.quantity_sold,
        s.price,
        s.date,
        c.customer_name,
        c.email
    FROM
        sales s
    JOIN
        customers c ON s.customer_id = c.customer_id
'''

result_df = pd.read_sql_query(query, db)

print("Joined Data:")
print(result_df)

db.close()
