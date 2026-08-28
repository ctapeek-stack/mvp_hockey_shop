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
password = input('Пароль: ')

sql = """
    SELECT customer_id, password_hash
    FROM customers
    WHERE email = %s;
    """
cur.execute(sql, (email,))
row = cur.fetchone()

if row is None:
    print('Пользователь не найден')
else:
    customer_id, password_hash = row
    password_bytes = password.encode('utf-8')
    hash_bytes = password_hash.encode('utf-8')

    if bcrypt.checkpw(password_bytes, hash_bytes):
        print(f"Вход выполнен! id = {customer_id}")
    else:
        print("Неверный пароль.")    

cur.close()
conn.close()


