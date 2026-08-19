SELECT products.product_name, products.price, categories.category_name #Таблица цен
FROM products
JOIN categories ON products.category_id = categories.category_id
ORDER BY products.price;

SELECT products.product_name, products.price, categories.category_name #Таблица цен по категориям
FROM products
JOIN categories ON products.category_id = categories.category_id 
WHERE category_name = 'Коньки'
ORDER BY products.price;

SELECT #Топ популярных товаров по продажам
products.product_name, 
SUM(quantity) AS total_sold
FROM order_items 
JOIN products ON order_items.product_id = products.product_id
GROUP BY products.product_id, products.product_name 
ORDER BY total_sold DESC, products.product_name
LIMIT 5;

SELECT product_name, stock #Товары с минимальными остатками на складе (<10)
FROM products
WHERE stock < 10
ORDER BY stock;