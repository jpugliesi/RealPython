import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT DISTINCT inventory.make, inventory.model, 
                                 inventory.quantity, orders.order_date FROM inventory, orders
                                 WHERE 
                                 inventory.make = orders.make ORDER BY inventory.make ASC""")

    rows = c.fetchall()

    for r in rows:
        print r[0]
        print r[1]
        print r[2]
        print r[3]
