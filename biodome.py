import tkinter as tk
from plant import (Orchid , Strawberry , Bonsai , JadeVine   )

class BioDome:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bio Dome Plant")
        self.root.geometry("500x500")
        self.current_plant = None
        self.outside_temperature = 28
        self.dome_temperature = 21
        self.moisture = 50
        self.home_button = tk.Button(
            self.root,
            text = "Home",
            command = self.go_home
        )
        self.water_button = tk.Button(
            self.root ,
            text = "water",
            command = self.water_plant
        )
        self.heat_button = tk.Button(
            self.root ,
            text = "Heat",
            command = self.heat_plant
        )
        self.vent_button = tk.Button(
            self.root ,
            text = "Ventilate",
            command = self.vent_plant
        )
        self.plants = [
    (Orchid, "Royal Orchid"),
    (Strawberry, "Wild Strawberry"),
    (Bonsai, "Mini Bonsai"),
    (JadeVine, "Jade Vine")
]
        self.title_label = tk.Label(
            self.root ,
            text = "Choose your plant",
            font=("Arial" , 18),
            background = "olive"

              )
        self.title_label.pack(pady = 10)
        self.stats_label = tk.Label(
            self.root , 
            text = "No plant has been selected!",
            foreground = "#556B2F",
        )
        self.stats_label.pack(pady=10)

        self.plant_buttons =[]
        for plant_class , name in self.plants:
         button = tk.Button(
        self.root,
        text=name,
        command=lambda pc=plant_class, n=name: self.choose_plant(pc, n)
    )
         button.pack(pady=5)
         self.plant_buttons.append(button)
         


    def choose_plant(self, plant_class, name):
      self.current_plant = plant_class(name)
      self.title_label.config(
          text = f"{self.current_plant.name} Dashboard"
      )

      for button in self.plant_buttons:
          button.pack_forget()
      self.update_stats()
      self.water_button.pack(pady=5)
      self.heat_button.pack(pady=5)
      self.vent_button.pack(pady=5)
      self.home_button.pack(pady=10)

    

    def water_plant(self):
        self.moisture = max(100 ,self.moisture + 1 )
        self.update_stats()
    
    def vent_plant(self):
        self.dome_temperatue -= 2
        self.update_stats()
       
    def heat_plant(self):
        self.dome_temperatue += 2
        self.update_stats()
       


    def update_stats(self):
        self.stats_label.config(
            text = 
            f"Name: {self.current_plant.name}\n"
            f"Health:{self.current_plant.health}\n"
            f"Level:{self.current_plant.level}\n"
            f"Coins:{self.current_plant.coins}\n"
            f"Outside Temp: {self.outside_temperature}°C\n"
            f"Bio-Dome Temp: {self.temperature}°C\n"
            f"Moisture: {self.moisture}%\n"
            f"Ideal Temp: {self.current_plant.ideal_temp}°C"
            f"Status:{status}"

        )
        difference = abs
        (self.dome_temperature -
        self.current_plant.ideal_temp
        )
        if difference <= 2 :
            status = "Comfortable"
        elif difference <= 5:
            status =  "Needs Attention"
        else:
            status = "Critical"

     
    def go_home(self):
        self.current_plant = None
        
        self.water_button.pack_forget()
        self.heat_button.pack_forget()
        self.vent_button.pack_forget()
        self.home_button.pack_forget()

        for button in self.plant_buttons:
         button.pack(pady=10)

        self.title_label.config(
           text="Choose Another plant"
)
         

        self.stats_label.config(
            text = "No plant has been selected"
        )
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
        app = BioDome()
        app.run()



