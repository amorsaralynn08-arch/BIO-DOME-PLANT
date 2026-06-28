from plant import Orchid, Strawberry, Bonsai, JadeVine
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
     cur.execute(''' 
                 INSERT INTO plants(name , level , xp , health , moisture , temperature , coins , plant_type)
                 VALUES (? , ? , ? , ? , ? , ? , ? , ?)
                 ''',(
                 plant.name,
                 plant.level,
                 plant.xp,
                 plant.health,
                 plant.moisture,
                 dome_temperature,
                 plant.coins,
                 plant.__class__.__name__
                 )
)
con.commit()

def load_plant(id):
     cur.execute('''SELECT * FROM plants
                 WHERE id = ?'''
                 (id,))
     
     plant_data = cur.fetchone()

     if plant_data is None:
        return None

     if plant_data[8] == "Orchid":
      plant = Orchid(plant_data[1])

     elif plant_data[8] == "Strawberry":
        plant = Strawberry(plant_data[1])

     elif plant_data[8] == "Bonsai":
        plant = Bonsai(plant_data[1])

     else:
        plant = JadeVine(plant_data[1])

     plant.level = plant_data[2]
     plant.xp = plant_data[3]
     plant.health = plant_data[4]
     plant.moisture = plant_data[5]
     plant.ideal_temp = plant_data[6]
     plant.coins = plant_data[7]

     return plant