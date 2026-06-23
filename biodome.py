import tkinter as tk
from plant import (Orchid , Strawberry , Bonsai , JadeVine   )

class BioDome:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bio Dome Plant")
        self.root.geometry("500x500")
        self.current_plant = None
        self.home_button = tk.Button(
            self.root,
            text = "Home",
            command = self.go_home
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
      self.home_button.pack(pady=10)


    def update_stats(self):
        self.stats_label.config(
            text = 
            f"Name: {self.current_plant.name}\n"
            f"Health:{self.current_plant.health}\n"
            f"Level:{self.current_plant.level}\n"
            f"Coins:{self.current_plant.coins}"

        )

     
    def go_home(self):
        self.current_plant = None
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



