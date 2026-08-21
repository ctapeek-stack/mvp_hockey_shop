import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


conn = psycopg.connect(    
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
    dbname=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
)

cur = conn.cursor()
limit = int(input('Максимальная цена: '))

sql = """
    SELECT products.product_name, products.price, categories.category_name
    FROM products
    JOIN categories ON products.category_id = categories.category_id
    WHERE products.price < %s
    ORDER BY products.price;
"""
cur.execute(sql, (limit,))

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
