import os

import bcrypt
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

email = input('Email: ')
product_id = int(input('id товара: '))
quantity = int(input('Колличество: '))

cur.execute("SELECT customer_id FROM customers WHERE email = %s;", (email,), )
row = cur.fetchone()
if row is None:
    print('Пользователь не найден')
    raise SystemExit
customer_id = row[0]

cur.execute("SELECT price, stock FROM products WHERE product_id = %s;", (product_id,), )
row = cur.fetchone()
if row is None:
    print('Товар не найден')
    raise SystemExit
price, stock = row

if stock < quantity:
    print(f"Недостаточно товара на складе: остаток {stock}")
    raise SystemExit

total = price * quantity

cur.execute("""
    INSERT INTO orders (customer_id, status, total_amount)
    VALUES (%s, 'new', %s)
    RETURNING order_id;""", (customer_id, total),)
order_id = cur.fetchone()[0]

cur.execute ("""
    INSERT INTO order_items (order_id, product_id, quantity, unit_price)
    VALUES (%s, %s, %s, %s);""", (order_id, product_id, quantity, price))

cur.execute("""
    UPDATE products
    SET stock = stock - %s
    WHERE product_id = %s;""", (quantity, product_id),)

conn.commit()

print(f"Заказ №{order_id} создан: {quantity} шт. на {total:.2f} руб.")

cur.close()
conn.close()
