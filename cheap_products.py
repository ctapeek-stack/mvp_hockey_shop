from db import get_connection

conn = get_connection()
cur = conn.cursor()

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
    print(f"{row[0]} - {row[1]:.2f} руб. ({row[2]})")

cur.close()
conn.close()
