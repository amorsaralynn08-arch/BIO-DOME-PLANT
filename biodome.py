import customtkinter as ctk
import time
from plant import Orchid, Strawberry, Bonsai, JadeVine
from weather import get_data

# ── Design tokens ────────────────────────────────────────────────────────────
FONT_DISPLAY   = ("Georgia", 22, "bold")
FONT_HEADING   = ("Georgia", 15, "bold")
FONT_BODY      = ("Helvetica Neue", 12)
FONT_LABEL     = ("Helvetica Neue", 11)
FONT_BTN       = ("Helvetica Neue", 12, "bold")

# Neutral surface palette (home screen)
BG_HOME        = "#F0F4F0"
CARD_HOME      = "#FFFFFF"
ACCENT_GREEN   = "#2E7D32"
ACCENT_LIGHT   = "#A5D6A7"
TEXT_PRIMARY   = "#1B2B1B"
TEXT_SECONDARY = "#5A7360"

# Per-plant accent palettes  {name: (bg, card, accent, btn)}
PLANT_THEMES = {
    "Royal Orchid":    ("#F3EEFF", "#EDE1FF", "#7B2FBE", "#9C4FDB"),
    "Wild Strawberry": ("#FFF0F3", "#FFE0E6", "#C0392B", "#E05C6A"),
    "Mini Bonsai":     ("#EBF5EB", "#D6EED6", "#2E7D32", "#4CAF50"),
    "Jade Vine":       ("#E6F7F7", "#CCF0F0", "#00796B", "#26A69A"),
}

HEALTH_COLOR = "#E91E63"
XP_COLOR     = "#43A047"

class BioDome:
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.root = ctk.CTk()
        self.root.title("Bio Dome Plant")
        self.root.geometry("720x700")
        self.root.resizable(False, False)
        self.root.configure(fg_color=BG_HOME)

        # ── Header bar ───────────────────────────────────────────────────────
        self.header_frame = ctk.CTkFrame(
            self.root, fg_color=ACCENT_GREEN, corner_radius=0, height=56
        )
        self.header_frame.pack(fill="x")
        self.header_frame.pack_propagate(False)

        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="🌿  Bio Dome",
            font=FONT_DISPLAY,
            text_color="#FFFFFF",
            fg_color="transparent",
        )
        self.title_label.pack(side="left", padx=24, pady=12)

        # ── Progress bars (hidden until a plant is chosen) ───────────────────
        self.progress_frame = ctk.CTkFrame(
            self.root, fg_color="transparent", corner_radius=0
        )

        self.health_frame = ctk.CTkFrame(
            self.progress_frame, fg_color=CARD_HOME, corner_radius=10
        )
        self.xp_frame = ctk.CTkFrame(
            self.progress_frame, fg_color=CARD_HOME, corner_radius=10
        )

        self.health_text = ctk.CTkLabel(
            self.health_frame,
            text="Health : 100%",
            font=FONT_LABEL,
            text_color=TEXT_PRIMARY,
        )
        self.health_bar = ctk.CTkProgressBar(
            self.health_frame,
            width=260,
            height=14,
            progress_color=HEALTH_COLOR,
            fg_color="#F5C6D6",
        )
        self.health_bar.set(1)

        self.xp_text = ctk.CTkLabel(
            self.xp_frame,
            text="XP: 0/50",
            font=FONT_LABEL,
            text_color=TEXT_PRIMARY,
        )
        self.xp_bar = ctk.CTkProgressBar(
            self.xp_frame,
            width=260,
            height=14,
            progress_color=XP_COLOR,
            fg_color="#C8E6C9",
        )
        self.xp_bar.set(0)

        self.health_text.pack(padx=14, pady=(10, 2))
        self.health_bar.pack(padx=14, pady=(0, 10))
        self.xp_text.pack(padx=14, pady=(10, 2))
        self.xp_bar.pack(padx=14, pady=(0, 10))

        self.health_frame.pack(side="left", padx=10, pady=12)
        self.xp_frame.pack(side="left", padx=10, pady=12)

        self.progress_frame.pack_forget()

        # ── Info cards (plant / environment / status) ─────────────────────────
        self.cards_frame = ctk.CTkFrame(self.root, fg_color="transparent")

        self.plant_frame = ctk.CTkFrame(
            self.cards_frame, corner_radius=12, border_width=0
        )
        self.environment_frame = ctk.CTkFrame(
            self.cards_frame, corner_radius=12, border_width=0
        )
        self.status_frame = ctk.CTkFrame(
            self.cards_frame, corner_radius=12, border_width=0
        )

        self.plant_label = ctk.CTkLabel(
            self.plant_frame,
            text="No plant selected",
            font=FONT_BODY,
            justify="left",
            anchor="nw",
        )
        self.environment_label = ctk.CTkLabel(
            self.environment_frame,
            text="Environment data",
            font=FONT_BODY,
            justify="left",
            anchor="nw",
        )
        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Status",
            font=FONT_HEADING,
            justify="center",
        )

        # ── Action buttons ────────────────────────────────────────────────────
        self.button_frame = ctk.CTkFrame(self.root, fg_color="transparent")

        _btn_cfg = dict(
            font=FONT_BTN,
            corner_radius=10,
            height=40,
            border_width=0,
        )

        self.water_button = ctk.CTkButton(
            self.root,
            text="💧  Water",
            command=self.water_plant,
            fg_color="#1565C0",
            hover_color="#1976D2",
            text_color="#FFFFFF",
            **_btn_cfg,
        )
        self.heat_button = ctk.CTkButton(
            self.root,
            text="🔥  Heat",
            command=self.heat_plant,
            fg_color="#BF360C",
            hover_color="#D84315",
            text_color="#FFFFFF",
            **_btn_cfg,
        )
        self.vent_button = ctk.CTkButton(
            self.root,
            text="🌬  Ventilate",
            command=self.vent_plant,
            fg_color="#00695C",
            hover_color="#00796B",
            text_color="#FFFFFF",
            **_btn_cfg,
        )
        self.home_button = ctk.CTkButton(
            self.root,
            text="⌂  Home",
            command=self.go_home,
            fg_color=ACCENT_GREEN,
            hover_color="#388E3C",
            text_color="#FFFFFF",
            **_btn_cfg,
        )

        self.button_frame.pack_forget()

        # ── Plant selection (home screen) ─────────────────────────────────────
        self.current_plant = None
        self.plant_themes = {
            "Royal Orchid":    "#E6E6FA",   # kept for go_home root color ref
            "Wild Strawberry": "#FFE4E1",
            "Mini Bonsai":     "#98FB98",
            "Jade Vine":       "#AFEEEE",
        }

        self.last_weather_update = time.time()
        self.game_loop()

        self.outside_temperature, self.outside_humidity = get_data()
        self.dome_temperature = 21

        self.plants = [
            (Orchid,     "Royal Orchid"),
            (Strawberry, "Wild Strawberry"),
            (Bonsai,     "Mini Bonsai"),
            (JadeVine,   "Jade Vine"),
        ]

        # Subtitle shown on home screen
        self.home_subtitle = ctk.CTkLabel(
            self.root,
            text="Choose your plant to begin",
            font=("Helvetica Neue", 13),
            text_color=TEXT_SECONDARY,
            fg_color="transparent",
        )
        self.home_subtitle.pack(pady=(22, 4))

        # Plant selection cards
        _plant_icons = {
            "Royal Orchid":    "🌸",
            "Wild Strawberry": "🍓",
            "Mini Bonsai":     "🌳",
            "Jade Vine":       "🌿",
        }

        self.plant_buttons = []
        for plant_class, name in self.plants:
            icon = _plant_icons.get(name, "🌱")
            btn = ctk.CTkButton(
                self.root,
                text=f"{icon}  {name}",
                command=lambda pc=plant_class, n=name: self.choose_plant(pc, n),
                font=FONT_BTN,
                fg_color=CARD_HOME,
                hover_color=ACCENT_LIGHT,
                text_color=TEXT_PRIMARY,
                corner_radius=12,
                border_width=1,
                border_color=ACCENT_LIGHT,
                height=48,
                width=260,
            )
            btn.pack(pady=7)
            self.plant_buttons.append(btn)

    # ── choose_plant (logic unchanged, only UI calls updated) ─────────────────
    def choose_plant(self, plant_class, name):
        self.current_plant = plant_class(name)

        bg, card, accent, btn_color = PLANT_THEMES.get(
            name, ("#F5F5F5", "#EBEBEB", ACCENT_GREEN, ACCENT_GREEN)
        )

        # Root & header
        self.root.configure(fg_color=bg)
        self.header_frame.configure(fg_color=accent)

        # Cards
        for frame in (self.plant_frame, self.environment_frame, self.status_frame):
            frame.configure(fg_color=card)
        for lbl in (self.plant_label, self.environment_label, self.status_label):
            lbl.configure(fg_color=card)

        # Progress bar cards
        for f in (self.health_frame, self.xp_frame):
            f.configure(fg_color=card)
        for lbl in (self.health_text, self.xp_text):
            lbl.configure(fg_color=card)

        # Action buttons tinted to plant accent
        self.water_button.configure(fg_color="#1565C0",  hover_color="#1976D2")
        self.heat_button.configure(fg_color="#BF360C",   hover_color="#D84315")
        self.vent_button.configure(fg_color="#00695C",   hover_color="#00796B")
        self.home_button.configure(fg_color=accent,      hover_color=btn_color)

        # Update header title
        self.title_label.configure(
            text=f"🌿  {self.current_plant.name} Dashboard"
        )

        # Hide home elements
        self.home_subtitle.pack_forget()
        for button in self.plant_buttons:
            button.pack_forget()

        # Show progress
        self.progress_frame.pack(fill="x", padx=24, pady=(8, 0))

        # Show info cards side by side
        self.cards_frame.pack(fill="x", padx=24, pady=8)
        self.plant_frame.pack(in_=self.cards_frame, side="left", fill="both",
                              expand=True, padx=(0, 6))
        self.environment_frame.pack(in_=self.cards_frame, side="left", fill="both",
                                    expand=True, padx=6)
        self.status_frame.pack(in_=self.cards_frame, side="left", fill="both",
                               expand=True, padx=(6, 0))

        self.plant_label.pack(pady=12, padx=14, fill="both", expand=True)
        self.environment_label.pack(pady=12, padx=14, fill="both", expand=True)
        self.status_label.pack(pady=12, padx=14, fill="both", expand=True)

        # Show action buttons
        self.button_frame.pack(pady=16)
        self.water_button.pack(in_=self.button_frame, side="left",
                               ipadx=8, padx=8)
        self.heat_button.pack(in_=self.button_frame, side="left",
                              ipadx=8, padx=8)
        self.vent_button.pack(in_=self.button_frame, side="left",
                              ipadx=8, padx=8)
        self.home_button.pack(in_=self.button_frame, side="left",
                              ipadx=8, padx=8)

        self.water_button.configure(state="normal")
        self.heat_button.configure(state="normal")
        self.vent_button.configure(state="normal")

        self.update_stats()

    # ── Unchanged logic methods ───────────────────────────────────────────────
    def water_plant(self):
        self.current_plant.moisture = min(100, self.current_plant.moisture + 10)
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

        difference = abs(self.dome_temperature - self.current_plant.ideal_temp)

        if difference < 2:
            status = "Comfortable"
            color = "#2E7D32"
        elif difference < 5:
            status = "Needs Attention"
            color = "#E65100"
        else:
            status = "Critical"
            color = "#B71C1C"

        moisture_difference = abs(
            self.current_plant.moisture - self.current_plant.ideal_moisture
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
            text=(
                f"ENVIRONMENT\n\n"
                f"Outside Temp: {self.outside_temperature}°C\n"
                f"Bio-Dome Temp: {self.dome_temperature}°C\n"
                f"Moisture: {self.current_plant.moisture}%\n"
                f"Moisture Status: {moisture_status}\n"
                f"Ideal Moisture: {self.current_plant.ideal_moisture}%\n"
                f"Outside Humidity: {self.outside_humidity}%\n"
                f"Ideal Temp: {self.current_plant.ideal_temp}°C"
            )
        )

        if status == "Comfortable" and moisture_condition == "Good":
            overal_status = "Healthy"
        elif status == "Critical" or moisture_condition == "Critical":
            overal_status = "Critical"
        else:
            overal_status = "Needs Attention"

        self.status_label.configure(
            text=f"STATUS\n\n{overal_status}",
            text_color=color,
        )
        self.health_bar.set(self.current_plant.health / 100)
        self.health_text.configure(
            text=f"Health:{self.current_plant.health}%"
        )

        if self.dome_temperature < self.outside_temperature:
            self.dome_temperature += 1
        elif self.dome_temperature > self.outside_temperature:
            self.dome_temperature -= 1

        if status == "Comfortable" and moisture_condition == "Good":
            self.current_plant.health = min(100, self.current_plant.health + 1)
            self.current_plant.xp += 1
            self.current_plant.coins += 1

            if self.current_plant.xp >= self.current_plant.level * 50:
                self.current_plant.level += 1

            current_xp = self.current_plant.xp % 50
            self.xp_bar.set(current_xp / 50)
            self.xp_text.configure(text=f"XP:{current_xp}/50")
        else:
            self.current_plant.health = max(0, self.current_plant.health - 1)

        self.plant_label.configure(
            text=(
                f"PLANT\n\n"
                f"Name: {self.current_plant.name}\n"
                f"Health: {self.current_plant.health}\n"
                f"Level: {self.current_plant.level}\n"
                f"Coins: {self.current_plant.coins}\n"
                f"XP:{self.current_plant.xp}\n"
                f"Next Level {self.current_plant.level * 50 } XP"
            )
        )

        if self.current_plant.health <= 0:
            self.water_button.configure(state="disabled")
            self.heat_button.configure(state="disabled")
            self.vent_button.configure(state="disabled")

    def game_loop(self):
        if self.current_plant:
            self.current_plant.moisture = max(
                0, self.current_plant.moisture - 1
            )
            self.update_stats()
        self.root.after(1000, self.game_loop)

    def go_home(self):
        self.current_plant = None

        self.root.configure(fg_color=BG_HOME)
        self.header_frame.configure(fg_color=ACCENT_GREEN)
        self.title_label.configure(text="🌿  Bio Dome")

        for lbl in (self.plant_label, self.environment_label, self.status_label):
            lbl.configure(fg_color=CARD_HOME)
        for f in (self.plant_frame, self.environment_frame, self.status_frame):
            f.configure(fg_color=CARD_HOME)
        for f in (self.health_frame, self.xp_frame):
            f.configure(fg_color=CARD_HOME)

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
        self.cards_frame.pack_forget()
        self.button_frame.pack_forget()
        self.progress_frame.pack_forget()

        self.home_subtitle.configure(text="Choose another plant")
        self.home_subtitle.pack(pady=(22, 4))

        for button in self.plant_buttons:
            button.pack(pady=7)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = BioDome()
    app.run()