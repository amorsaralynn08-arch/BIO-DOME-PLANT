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



