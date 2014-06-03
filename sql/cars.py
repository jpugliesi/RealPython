import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars_to_add = [
                    ('Ford', 'Taurus', 20),
                    ('Ford', 'F150', 50),
                    ('Ford', 'Escape', 23),
                    ('Honda', 'Civic', 10),
                    ('Honda', 'CRV', 12)
                  ]

    c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", cars_to_add)

