import tkinter as tk
from plant import (Orchid , Strawberry , Bonsai , JadeVine   )

class BioDome:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bio Dome Plant")
        self.root.geometry("500x500")
        self.current_plant = None
        self.title_label = tk.Label(
            self.root ,
            text = "Choose your plant",
            font=("Arial" , 18),
            background = "skyblue"

              )
        self.title_label.pack(pady = 10)
        self.stats_label = tk.Label(
            self.root , 
            text = "No plant has been selected!",
            foreground = "#556B2F",
        )
        self.stats_label.pack(pady=10)
        tk.Button(self.root, 
                  text="Orchid", 
                  command=lambda: self.choose_plant(Orchid, "Royal Orchid")
                  ).pack(pady=10)
        tk.Button(self.root,
                   text="Strawberry", 
                   command=lambda: self.choose_plant(Strawberry, "Wild Strawberry")
                   ).pack(pady=10)
        tk.Button(self.root,
                   text="Bonsai", 
                   command=lambda: self.choose_plant(Bonsai, "Bonsai")
                   ).pack(pady=10)
        tk.Button(self.root,
                   text="JadeVine", 
                   command=lambda: self.choose_plant(JadeVine, "JadeVine")
                   ).pack(pady=10)


    def choose_plant(self, plant_class, name):
     self.current_plant = plant_class(name)
     self.update_stats()


    def update_stats(self):
        self.stats_label.config(
            text = 
            f"Name: {self.current_plant.name}\n"
            f"Health:{self.current_plant.health}\n"
            f"Level:{self.current_plant.level}\n"
            f"Coins:{self.current_plant.coins}"

        )
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
        app = BioDome()
        app.run()



