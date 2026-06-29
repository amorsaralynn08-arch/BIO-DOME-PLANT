import customtkinter as ctk
import time  # Kept to handle the 30-second weather refresh rate
from plant import Orchid, Strawberry, Bonsai, JadeVine
from weather import get_data

class BioDome:
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.root = ctk.CTk()
        self.root.title("Bio Dome Plant")
        self.root.geometry("700x650")
        
        self.plant_frame = ctk.CTkFrame(
            self.root,
            border_width=2
        )

        self.environment_frame = ctk.CTkFrame(
            self.root,
            border_width=2
        )
        
        self.status_frame = ctk.CTkFrame( 
            self.root,
            border_width=2
        )
        self.progress_frame = ctk.CTkFrame(self.root)
        self.progress_frame.pack(pady=10)

        self.button_frame = ctk.CTkFrame(self.root)
        self.health_frame = ctk.CTkFrame(self.progress_frame)
        self.xp_frame = ctk.CTkFrame(self.progress_frame)

        self.health_bar = ctk.CTkProgressBar(
            self.health_frame,
            width=250,
            progress_color="#FF69B4"
        )
        self.health_bar.set(1)
        self.health_text = ctk.CTkLabel(
            self.health_frame,
            text = "Health : 100%"
        )
        self.xp_bar = ctk.CTkProgressBar(
           self.xp_frame,
           width=250,
           progress_color="#228B22"
        )
        self.xp_bar.set(0)
        
        self.xp_text = ctk.CTkLabel(
            self.xp_frame,
            text = "XP: 0/50"
        )

        self.health_text.pack()
        self.health_bar.pack()

        self.xp_text.pack()
        self.xp_bar.pack()

        self.health_frame.pack(side="left", padx=10)
        self.xp_frame.pack(side="left", padx=10)

        self.progress_frame.pack_forget()
        self.button_frame.pack_forget()
      
        self.current_plant = None
        self.plant_themes = {
            "Royal Orchid": "#E6E6FA",
            "Wild Strawberry": "#FFE4E1",
            "Mini Bonsai": "#98FB98",
            "Jade Vine": "#AFEEEE"
        }
        
        # Tracking variables for performance
        self.last_weather_update = 0  
        self.loop_is_running = False  

        self.outside_temperature, self.outside_humidity = get_data()
        self.dome_temperature = 21
        self.home_button = ctk.CTkButton(
            self.root,
            text = "Home",
            command = self.go_home,
            fg_color="#228B22",
        )
        self.water_button = ctk.CTkButton(
            self.root ,
            text = "water",
            command = self.water_plant,
            fg_color="lightgreen",
            text_color="black"
        )
        self.heat_button = ctk.CTkButton(
            self.root ,
            text = "Heat",
            command = self.heat_plant,
            fg_color="lightgreen",
            text_color="black"
        )
        self.vent_button = ctk.CTkButton(
            self.root ,
            text = "Ventilate",
            command = self.vent_plant,
            fg_color="lightgreen",
            text_color="black"
        )
        self.plants = [
            (Orchid, "Royal Orchid"),
            (Strawberry, "Wild Strawberry"),
            (Bonsai, "Mini Bonsai"),
            (JadeVine, "Jade Vine")
        ]
        
        self.title_label = ctk.CTkLabel(
            self.root ,
            text = "Choose your plant",
            font=("Arial" , 18),
            fg_color = "olive"
        )
        self.title_label.pack(pady = 10)

        self.plant_label = ctk.CTkLabel(
            self.plant_frame,
            text="No plant selected",
            font=("Arial", 12),
            width = 60
        )

        self.environment_label = ctk.CTkLabel(
            self.environment_frame,
            text="Environment data",
            font=("Arial", 12),
            width = 60
        )

        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Status",
            font=("Arial", 14, "bold"),
            width = 30
        )
        
        self.plant_buttons = []
        for plant_class , name in self.plants:
            button = ctk.CTkButton(
                self.root,
                text=name,
                command=lambda pc=plant_class, n=name: self.choose_plant(pc, n)
            )
            button.pack(pady=5)
            self.plant_buttons.append(button)

    def choose_plant(self, plant_class, name):
        self.current_plant = plant_class(name)
        
        # Start the loop if it's not running yet
        if not self.loop_is_running:
            self.loop_is_running = True
            self.game_loop()
            
        theme = self.plant_themes.get(name , "white")
        self.root.configure(fg_color=theme)
        self.title_label.configure(fg_color=theme)
        self.plant_label.configure(fg_color=theme)
        self.environment_label.configure(fg_color=theme)
        self.status_label.configure(fg_color=theme)
        self.progress_frame.pack(pady=10)
        self.plant_frame.pack( padx=20, pady=5)
        self.environment_frame.pack( padx=20, pady=5)
        self.status_frame.pack( padx=20, pady=5)
        self.plant_frame.configure(fg_color=theme)
        self.environment_frame.configure(fg_color=theme)
        self.status_frame.configure(fg_color=theme)
        
        self.button_frame.pack(pady=20)

        self.water_button.pack(in_=self.button_frame, side="left", ipady=5, ipadx=10, padx=5)
        self.heat_button.pack(in_=self.button_frame, side="left", ipady=5, ipadx=10, padx=5)
        self.vent_button.pack(in_=self.button_frame, side="left", ipady=5, ipadx=10, padx=5)
        self.home_button.pack(in_=self.button_frame, side="left", ipady=5, ipadx=10, padx=5)
        self.title_label.configure(
            text = f"{self.current_plant.name} Dashboard"
        )
        self.water_button.configure(state = "normal")
        self.heat_button.configure(state = "normal")
        self.vent_button.configure(state = "normal")

        for button in self.plant_buttons:
            button.pack_forget()
        self.update_stats()
        self.plant_label.pack(pady=10 , padx = 10)
        self.environment_label.pack(pady=10 , padx = 10)
        self.status_label.pack(pady=10 , padx = 10)

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
        current_time = time.time()
        if current_time - self.last_weather_update > 30:
            self.outside_temperature, self.outside_humidity = get_data()
            self.last_weather_update = current_time

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
        
        self.environment_label.configure(
            text=
            f"ENVIRONMENT\n\n"
            f"Outside Temp: {self.outside_temperature}°C\n"
            f"Bio-Dome Temp: {self.dome_temperature}°C\n"
            f"Moisture: {self.current_plant.moisture}%\n"
            f"Moisture Status: {moisture_status}\n"
            f"Ideal Moisture: {self.current_plant.ideal_moisture}%\n"
            f"Outside Humidity: {self.outside_humidity}%\n"
            f"Ideal Temp: {self.current_plant.ideal_temp}°C"
        )
        if status == "Comfortable" and moisture_condition == "Good":
            overal_status = "Healthy"
        elif status == "Critical" or moisture_condition == "Critical":
            overal_status = "Critical"
        else:
            overal_status = "Needs Attention"
            
        self.status_label.configure(
            text=f"STATUS\n\n{overal_status}",
            text_color = color
        )
        self.health_bar.set(self.current_plant.health / 100)
        self.health_text.configure(
            text = f"Health:{self.current_plant.health}%"
        )
        if self.dome_temperature < self.outside_temperature:
            self.dome_temperature += 1
        elif self.dome_temperature > self.outside_temperature:
            self.dome_temperature -= 1 

        if status == "Comfortable" and moisture_condition == "Good":
            self.current_plant.health = min(100, self.current_plant.health + 1 )
            self.current_plant.xp += 1
            self.current_plant.coins += 1

            if self.current_plant.xp >= self.current_plant.level * 50:
                self.current_plant.level += 1

            current_xp = self.current_plant.xp % 50
            self.xp_bar.set(current_xp / 50)
            self.xp_text.configure(
                text = f"XP:{current_xp}/50"
            )
        else:
            self.current_plant.health = max(0 , self.current_plant.health - 1)

        self.plant_label.configure(
            text=
            f"PLANT\n\n"
            f"Name: {self.current_plant.name}\n"
            f"Health: {self.current_plant.health}\n"
            f"Level: {self.current_plant.level}\n"
            f"Coins: {self.current_plant.coins}\n"
            f"XP:{self.current_plant.xp}\n"
            f"Next Level {self.current_plant.level * 50 } XP"
        )
        
        if self.current_plant.health <= 0:
            self.water_button.configure(state = "disabled")
            self.heat_button.configure(state = "disabled")
            self.vent_button.configure(state = "disabled")

    def game_loop(self):
        if self.current_plant:
            self.current_plant.moisture = max(0 , self.current_plant.moisture - 1)
            self.update_stats()
            self.root.after(1000, self.game_loop)

    def go_home(self):
        self.current_plant = None
        
        self.root.configure(fg_color="white")
        self.title_label.configure(fg_color="olive")
        self.plant_label.configure(fg_color="white")
        self.environment_label.configure(fg_color="white")
        self.status_label.configure(fg_color="white")
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
        self.button_frame.pack_forget()
        self.progress_frame.pack_forget()

        for button in self.plant_buttons:
            button.pack(pady=10)

        self.title_label.configure(text="Choose Another plant")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BioDome()
    app.run()