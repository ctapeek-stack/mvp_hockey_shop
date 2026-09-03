from db import get_connection
import bcrypt

conn = get_connection()
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
    row = cur.fetchone()
    conn.commit()
    print(f"Пользователь {email} зарегистрирован, id = {row[0]}")
except psycopg.errors.UniqueViolation:
    conn.rollback()
    print('Этот email уже зарегистрирован')

cur.close()
conn.close()
