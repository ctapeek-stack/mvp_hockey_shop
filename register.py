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

first_name = input('Имя: ')
last_name = input('Фамилия: ')
email = input('Email: ')
password = input('Пароль: ')

password_bytes = password.encode('utf-8')
salt = bcrypt.gensalt()
hash_bytes = bcrypt.hashpw(password_bytes, salt)
password_hash = hash_bytes.decode('utf-8')



sql = """
    INSERT INTO customers (first_name, last_name, email, password_hash)
    VALUES (%s, %s, %s, %s)
    RETURNING customer_id;
"""
try:
    cur.execute(sql, (first_name, last_name, email, password_hash))
    row = cur.fetchone
    conn.commit()
    print(f"Пользователь {email} зарегистрирован, id = {row[0]}")
except psycopg.errors.UniqueViolation:
    conn.rollback()
    print('Этот email уже зарегистрирован')

cur.close()
conn.close()
