# The following code is using to connect to the database and write an SQL query (You can also use a database IDE/software to run your queries).

import sqlite3

con = sqlite3.connect("/content/drive/MyDrive/Mis Documentos/Curso de Python/M) Python TUM/Customers.db")
c = con.cursor()

# List all the categories in the categories table.
categor = c.execute("SELECT * FROM categories")
cats = categor.fetchall()
#cats

# List the names and email addresses of all the customers in the customers table.
n_a = c.execute("SELECT first_name, email FROM customers")
n_a_1 = n_a.fetchall()
n_a_1

# List the names of all customers whose name starts with the letter "B".
B = c.execute("SELECT first_name, last_name FROM customers WHERE first_name LIKE 'B%' ")
B_a = B.fetchall()
#B_a

# List the names of all the customers in the customers table in alphabetical order.
A = c.execute("SELECT * FROM customers WHERE first_name IS NOT NULL ORDER BY first_name ASC")
A_a = A.fetchall()
#A_a

# List the names and email addresses of all the customers in the customers table who have ordered something.
O = c.execute("SELECT customers.first_name, customers.email FROM customers INNER JOIN orders ON customers.customer_id = orders.customer_id")
O_a = O.fetchall()
# O_a

# List the names and email addresses of all the customers in the customers table who have not ordered anything.
N = c.execute("SELECT first_name, email FROM customers WHERE customer_id NOT IN(SELECT customer_id FROM orders)")
N_a = N.fetchall()
# N_a

# List the names of all the customers who have made orders in the month of January 2023.
J = c.execute("SELECT customers.first_name, customers.email FROM customers INNER JOIN orders ON customers.customer_id = orders.customer_id WHERE strftime('%m',orders.order_date) = '01' ")
J_a = J.fetchall()
# J_a

# List all customers with their personal information and each order they make it.
I = c.execute("SELECT customers.first_name, customers.last_name, customers.email, order_items.order_id FROM order_items INNER JOIN orders ON orders.order_id = order_items.order_id INNER JOIN customers ON orders.customer_id = customers.customer_id ORDER BY customers.first_name")
I_a = I.fetchall()
# I_a

# List the names of all the products and the total number of orders that each product has been a part of.
P = c.execute("SELECT products.product_name, SUM(order_items.quantity) AS sum_quantity FROM products INNER JOIN order_items ON products.product_id = order_items.product_id GROUP BY order_items.product_id")
P_a = P.fetchall()
# P_a
