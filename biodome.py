import tkinter as tk
from plant import (Orchid , Strawberry , Bonsai , JadeVine   )

class BioDome:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bio Dome Plant")
        self.root.geometry("700x650")
        
        
        

        self.plant_frame = tk.Frame(
        self.root,
        relief="solid",
        bd=2
)
    

        self.environment_frame = tk.Frame(
    self.root,
    relief="solid",
    bd=2
)
        
  

        self.status_frame = tk.Frame(
            self.root,
            relief="solid",
            bd=2
        )
      
        

        
  
        

        self.current_plant = None
        self.plant_themes = {
        "Royal Orchid": "#E6E6FA",
        "Wild Strawberry": "#FFE4E1",
        "Mini Bonsai": "#98FB98",
        "Jade Vine": "#AFEEEE"
}
        self.outside_temperature = 28
        self.dome_temperature = 21
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

        self.plant_label = tk.Label(
        self.plant_frame,
        text="No plant selected",
        font=("Arial", 12)
    )

        self.environment_label = tk.Label(
            self.environment_frame,
            text="Environment data",
            font=("Arial", 12)
        )

        self.status_label = tk.Label(
            self.status_frame,
            text="Status",
            font=("Arial", 14, "bold")
        )

        


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
      self.game_loop()
      theme = self.plant_themes.get(name , "white")
      self.root.config(bg=theme)
      self.title_label.config(bg=theme)
      self.plant_label.config(bg=theme)
      self.environment_label.config(bg=theme)
      self.status_label.config(bg=theme)
      self.plant_frame.pack(fill="x", padx=20, pady=5)
      self.environment_frame.pack(fill="x", padx=20, pady=5)
      self.status_frame.pack(fill="x", padx=20, pady=5)
      self.plant_frame.config(bg=theme)
      self.environment_frame.config(bg=theme)
      self.status_frame.config(bg=theme)
    
      self.title_label.config(
          text = f"{self.current_plant.name} Dashboard"
      )
      



      for button in self.plant_buttons:
          button.pack_forget()
      self.update_stats()
      self.plant_label.pack(pady=10 , padx = 10)

      self.environment_label.pack(pady=10 , padx = 10)

      self.status_label.pack(pady=10 , padx = 10)
      self.water_button.pack(pady=5)
      self.heat_button.pack(pady=5)
      self.vent_button.pack(pady=5)
      self.home_button.pack(pady=10)

    

    def water_plant(self):
        self.current_plant.moisture = min(100 ,self.current_plant.moisture + 10 )
        self.update_stats()
        
    
    def vent_plant(self):
        self.dome_temperature -= 2
        self.update_stats()
       
    def heat_plant(self):
        self.dome_temperature += 2
        self.update_stats()
       


    def update_stats(self):
        difference = abs(
        self.dome_temperature -
        self.current_plant.ideal_temp
        )
       
        if difference < 2 :
                status = "Comfortable"
                color = "green"
        elif difference < 5:
                status =  "Needs Attention"
                color = "orange"
        else:
                status = "Critical"
                color = "red"

        moisture_difference = abs(
       self.current_plant.moisture -
       self.current_plant.ideal_moisture
        )
        if moisture_difference <= 10:
         moisture_condition = "Good"

        elif moisture_difference <= 20:
         moisture_condition = "Needs Attention"

        else:
         moisture_condition = "Critical"
 

       
        if self.current_plant.moisture <= 20:
         moisture_status = "Dry"

        elif self.current_plant.moisture <= 40:
         moisture_status = "Low"

        elif self.current_plant.moisture <= 70:
         moisture_status = "Good"

        elif self.current_plant.moisture <= 90:
         moisture_status = "High"

        else:
         moisture_status = "Overwatered"
        

        self.environment_label.config(
        text=
        f"ENVIRONMENT\n\n"
        f"Outside Temp: {self.outside_temperature}°C\n"
        f"Bio-Dome Temp: {self.dome_temperature}°C\n"
        f"Moisture: {self.current_plant.moisture}%\n"
        f"Moisture Status: {moisture_status}\n"
        f"Ideal Moisture: {self.current_plant.ideal_moisture}%\n"
        f"Ideal Temp: {self.current_plant.ideal_temp}°C"
    )
        if status == "Comfortable" and moisture_condition == "Good":
            overal_status = "Healthy"
        elif status == "Critical" or moisture_condition in "Critical":
            overal_status = "Critical"
        else:
            overal_status = "Needs Attention"
        self.status_label.config(
        text=f"STATUS\n\n"
        f"{overal_status}",
        fg = color
    )
        if self.dome_temperature < self.outside_temperature:
            self.dome_temperature += 1
        elif self.dome_temperature > self.outside_temperature:
            self.dome_temperature -= 1 

        if status == "Comfortable" and moisture_condition == "Good":
            self.current_plant.health = min(100, self.current_plant.health + 1 )
            self.current_plant.coins += 1
        else:
            self.current_plant.health = max(0 , self.current_plant.health - 1)

        self.plant_label.config(
        text=
        f"PLANT\n\n"
        f"Name: {self.current_plant.name}\n"
        f"Health: {self.current_plant.health}\n"
        f"Level: {self.current_plant.level}\n"
        f"Coins: {self.current_plant.coins}"
    )


    
    def game_loop(self):
        if self.current_plant:
            self.current_plant.moisture = max(0 , self.current_plant.moisture - 1)
            self.update_stats()
            self.root.after(10000 , self.game_loop)


                    
        
    def go_home(self):
        self.current_plant = None
        self.root.config(bg="white")
        self.title_label.config(bg="olive")
        self.plant_label.config(bg="white")
        self.environment_label.config(bg="white")
        self.status_label.config(bg="white")
        self.plant_label.pack_forget()
        self.environment_label.pack_forget()
        self.status_label.pack_forget()
        self.water_button.pack_forget()
        self.heat_button.pack_forget()
        self.vent_button.pack_forget()
        self.home_button.pack_forget()
        self.plant_frame.pack_forget()
        self.environment_frame.pack_forget()
        self.status_frame.pack_forget()
        
  
  
  
        

        for button in self.plant_buttons:
         button.pack(pady=10)

        self.title_label.config(
           text="Choose Another plant"
)
         

    def run(self):
        
        self.root.mainloop()

if __name__ == "__main__":
        app = BioDome()
        app.run()



