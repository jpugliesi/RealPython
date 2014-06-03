import sqlite3
import csv

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    
    try:
        c.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
    except sqlite3.OperationalError:
        print "Oops! Something went wrong. Try again..."
