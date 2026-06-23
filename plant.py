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
 