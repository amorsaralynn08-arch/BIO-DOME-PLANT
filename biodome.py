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

