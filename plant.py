from abc import ABC, abstractmethod

class Plant(ABC):
 def __init__(self , name):
  self.name = name
  self.health = 100
  self.level = 1
  self.coins = 0

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



