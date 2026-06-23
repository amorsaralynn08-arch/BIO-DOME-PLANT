import tkinter as tk
from plant import (Orchid , Strawberry , Bonsai , JadeVine   )

class BioDome:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bio Dome Plant")
        self.root.geometry("500x500")
        self.current_plant = None
        self.title_label = tk.label(
            self.root ,
            text = "Choose your plant",
            font=("Arial" , 18),
            background = "sky-blue"

              )
        self.title_label.pack(pady = 10)
        self.stats_label = tk.Label(
            self.root , 
            text = "No plant has been selected!",
            foreground = 556B2F,
        )
        self.stats_label.pack(pady=10)
        tk.Button(
            self.root,
            text = "Orchid",
            command=self.choose_Orchid,
        ).pack(pady=10)
        tk.Button(
            self.root,
            text = "Strawberry",
            command=self.choose_Strawberry,
        ).pack(pady=10)
        tk.Button(
            self.root,
            text = "Bonsai",
            command=self.choose_Bonsai,
        ).pack(pady=10)
        tk.Button(
            self.root,
            text = "JadeVine",
            command=self.choose_JadeVine,
        ).pack(pady=10)

    def choose_Orchid(self):
        self.current_plant = Orchid("Royal Orchid")
        self.update_stats()

    def choose_Strawberry(self):
        self.current_plant = Strawberry("Strawberry")
        self.update_stats()

    def choose_JadeVine(self):
        self.current_plant = JadeVine("JadeVine")
        self.update_stats()
    
    def choose_Bonsai(self):
        self.current_plant = Bonsai("Bonsai")
        self.update_stats()




