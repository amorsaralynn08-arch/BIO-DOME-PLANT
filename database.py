#im using sqlite to store the plant data so it persiss even when out of session

import sqlite3

# establishing a connection with sqlite
con =sqlite3.connect('biodome.db')

#setting up a cursor to help execute commands on the db

cur = con.cursor()

#creating the db table 

cur.execute(''' CREATE TABLE IF NOT EXISTs plants
            (id INTEGER PRIMARY KEY AUTOINCREMENT
            name TEXT ,
            level INTEGER ,
            XP INTEGER ,
            health INTEGER ,
            moisture INTEGER ,
            temperature INTEGER ,
            coins INTEGER
            )''')