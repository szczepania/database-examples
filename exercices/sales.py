import sqlite3
import random
from faker import Faker
import pandas as pd

fake = Faker()

db = sqlite3.connect('../databases/database.db')
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        product_id INTEGER,
        product_name TEXT,
        quantity_sold INTEGER,
        price REAL,
        date TEXT
    )
''')

sample_data = [
    (
        i + 1,
        fake.word(),
        random.randint(1, 20),
        round(random.uniform(10, 100), 2),
        fake.date_between(start_date='-30d', end_date='today').strftime('%Y-%m-%d')
    )
    for i in range(51)
]

cursor.executemany('INSERT INTO sales VALUES (?, ?, ?, ?, ?)', sample_data)
db.commit()

df = pd.read_sql_query('SELECT * FROM sales', db)

total_sales = df['quantity_sold'] * df['price']
df['total_sales'] = total_sales
print(f"Total sales: {total_sales}")

monthly_sales = df.groupby(df['date'].str.slice(0, 7))['total_sales'].sum()

print(f"Monthly sales: {monthly_sales}")

highest_selling_product = pd.read_sql_query('SELECT * FROM sales ORDER BY quantity_sold DESC LIMIT 1', db)
print(f"Highest Selling Product: {highest_selling_product}")

db.close()
