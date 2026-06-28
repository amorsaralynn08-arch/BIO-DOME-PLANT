#im using sqlite to store the plant data so it persiss even when out of session

import sqlite3

# establishing a connection with sqlite
con =sqlite3.connect('biodome.db')

#setting up a cursor to help execute commands on the db

cur = con.cursor()

#creating the db table 

cur.execute(''' CREATE TABLE IF NOT EXISTS plants
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT ,
            level INTEGER ,
            XP INTEGER ,
            health INTEGER ,
            moisture INTEGER ,
            temperature INTEGER ,
            coins INTEGER,
            plant_type TEXT
            )''')

con.commit() #this saves the changes to the database

def save_plant(plant , dome_temperature):#Saves a plants data into the database
     cur.execute(''' INSERT INTO plants(name , level , xp , health , moisture , temperature , coins , plant_type)
                 VALUES (? , ? , ? , ? , ? , ? , ? , ?)
                 plant.name
                 plant.level
                 plant.xp
                 plant.health
                 plant.moisture
                 dome_temperature
                 plant.coins
                 plant.__class__.__name__

''')
con.commit()


