from db import get_connection
import bcrypt

conn = get_connection()
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


