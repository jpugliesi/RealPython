import sqlite3

connection = sqlite3.connect("cars.db")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE inventory
                (make TEXT, model TEXT, quantity INT)""")

connection.close()
