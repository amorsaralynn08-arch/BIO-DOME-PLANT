# Bio-Dome Plant System

## Project Description
The Bio-Dome Plant System is a Python desktop simulation of a digital plant living inside a controlled bio-dome environment. The plant reacts dynamically to user interactions (watering, heating, ventilation) and real-world weather data using an external API.

The system is built using Object-Oriented Programming (OOP), a Tkinter graphical user interface, weather API integration, and SQLite database storage for persistent plant state.

---

## Project Goal
The goal of this project is to simulate a living plant system that:
- Responds to user actions
- Reacts to real-world environmental conditions
- Maintains persistent state across sessions
- Demonstrates proper Python software architecture using OOP, GUI, API, and database integration

---

## End Goal (Project Completion Criteria)

The project is considered complete when:
- The plant updates health, moisture, and temperature correctly
- The system responds to real-time weather data via API
- Tkinter GUI displays plant stats and controls
- User can interact using buttons (water, heat, ventilate)
- Plant state is saved and loaded using SQLite database
- Application runs without errors and persists data between sessions

---

## Features
- Interactive digital plant simulation
- Real-time weather integration using API
- Graphical user interface using Tkinter
- Object-Oriented Programming structure
- Persistent storage using SQLite database
- Environment variable management using .env file

---

## Project Structure

Bio-Dome/
│
├── main.py              # Entry point of application


├── plant.py            # Plant class (handles plant logic and stats)


├── biodome.py          # Core system logic and UI controller


├── database.py         # SQLite database handling


│
├── requirements.txt    # Project dependencies


├── .env                # Environment variables (NOT pushed to GitHub)


├── .gitignore         # Files ignored by Git


├── README.md          # Project documentation


├── LICENSE            # MIT License file


├── venv/              # Virtual environment (NOT pushed to GitHub)

---

## Installation Guide

### 1. Clone the repository
```bash
git clone https://github.com/your-username/bio-dome.git
cd bio-dome
```

---

### 2. Create virtual environment
```bash
python -m venv venv
```

---

### 3. Activate virtual environment

Windows (Git Bash):
```bash
source venv/Scripts/activate
```

Windows (CMD):
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

---

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

---

### 5. Run the application
```bash
python main.py
```

---

## Installing Dependencies from Scratch

If starting from zero:

```bash
pip install requests python-dotenv
```

Then freeze dependencies:

```bash
pip freeze > requirements.txt
```

---

## Environment Variables (.env Setup)

Create a file named .env in the project root directory.

Add:

WEATHER_API_URL=https://api.open-meteo.com/v1/forecast

---

## How .env is Used in Python

Install dependency:

```bash
pip install python-dotenv
```

Example usage:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_url = os.getenv("WEATHER_API_URL")
```

---

## .gitignore Setup

Create a .gitignore file and include:

venv/
__pycache__/
.env
*.pyc

---

## API Used

The project uses the Open-Meteo Weather API (no API key required).

The system fetches real-time weather data to influence plant behavior:
- Rain increases moisture
- High temperature decreases moisture faster
- Weather conditions affect plant stability dynamically

---

## Database (SQLite)

The system uses SQLite to store persistent plant state.

Stored data includes:
- Plant health
- Moisture level
- Temperature
- Last saved session state

This allows the plant to retain its condition between sessions.

---

## OOP Structure

Plant class:
- Handles plant attributes (health, moisture, temperature)
- Contains methods for updating plant state

BioDome class:
- Controls application logic
- Manages UI interactions
- Connects API and database to the plant system

Database module:
- Handles saving and loading plant data

---

## Running the Project

After setup is complete:

```bash
python main.py
```

---

## Author
Saralynn Amor

---

## License
This project is licensed under the MIT License.

