import entity
import random

class Hero(entity.Entity):
  """Hero class inherited from Entity class"""
  
  def basic_attack(self, other):
    dmg = random.randint(1,6) + random.randint(1,6)
    other.take_damage(dmg)
    return f"You slash the {other.name} with your sword for {dmg} damage"

  def special_attack(self, other):
    dmg = random.randint(1,12)
    other.take_damage(dmg)
    return f"You hit the {other.name} with an arrow for {dmg} damage"


    