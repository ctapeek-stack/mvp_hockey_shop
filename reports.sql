-- 1. Каталог: все товары с ценами и категориями, по возрастанию цены
SELECT products.product_name, products.price, categories.category_name
FROM products
JOIN categories ON products.category_id = categories.category_id
ORDER BY products.price;

-- 2. Каталог категории: товары выбранной категории («Коньки»), по возрастанию цены
SELECT products.product_name, products.price, categories.category_name
FROM products
JOIN categories ON products.category_id = categories.category_id 
WHERE category_name = 'Коньки'
ORDER BY products.price;

-- 3. Хиты продаж: топ-5 товаров по числу проданных единиц
SELECT
products.product_name, 
SUM(quantity) AS total_sold
FROM order_items 
JOIN products ON order_items.product_id = products.product_id
GROUP BY products.product_id, products.product_name 
ORDER BY total_sold DESC, products.product_name
LIMIT 5;

-- 4. Склад: товары с остатком менее 10 шт., критичные первыми
SELECT product_name, stock
FROM products
WHERE stock < 10
ORDER BY stock;