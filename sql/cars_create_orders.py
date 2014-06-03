import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE orders (make TEXT, model TEXT, order_date TEXT)")
    orders = [
                ('Ford', 'Taurus', '2013-12-10'),
                ('Ford', 'Taurus', '2014-10-12'),
                ('Honda', 'Civic', '2012-09-09')
             ]

    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)
