from abc import ABC, abstractmethod

class Plant(ABC):
 def __init__(self , name):
  self.name = name
  self.health = 100
  self.level = 1
  self.coins = 0
  self.xp = 0
  self.moisture = 50

 @abstractmethod
 def grow(self):
      pass
 def is_alive(self):
      return self.health > 0
        
 def take_damage(self , amount):
      self.health = max(0, self.health - amount)
 def heal(self , amount , cost):
    if self.coins >= cost:
      self.coins -= cost
      self.health = min (100 , self.health + amount)
      return True
    return False
 def add_coins(self , amount):
    self.coins += amount
 def level_up(self):
   if self.health >= 80:
          self.level += 1
          self.coins += 10
 def status_checker(self):
    if self.health <= 0 :
     return "dead plant"
    elif self.health < 30:
     return "Critical"
    elif self.health < 50:
      return "unstable"
    elif self.health < 70 :
      return "stable"
    else :
      return "healthy"
        
 def reset(self):
    self.health = 100
    self.level = 1
    self.coins = 0



class Orchid(Plant):
   def __init__(self, name):
        super().__init__(name)
        self.ideal_temp = 28
        self.ideal_moisture = 40


   def grow(self):
    self.health = min(100, self.health + 2)
    self.add_coins(2)

class Strawberry(Plant):
   def __init__(self, name):
        super().__init__(name)
        self.ideal_temp = 20
        self.ideal_moisture = 50
    

   def grow(self):
    self.health =min(100, self.health + 3)
    self.add_coins(3)

class Bonsai(Plant):
   def __init__(self, name):
        super().__init__(name)
        self.ideal_temp = 24
        self.ideal_moisture = 62


   def grow(self):
    self.health = min(100, self.health + 1)
    self.add_coins(1)

class JadeVine(Plant):
   def __init__(self, name):
        super().__init__(name)
        self.ideal_temp = 30
        self.ideal_moisture = 45


   def grow(self):
    self.health = min(100, self.health + 4)
    self.add_coins(4)

plants = [
    Orchid("Orchid"),
    Strawberry("Strawberry"),
    Bonsai("Bonsai"),
    JadeVine("Jade Vine")
]


