import entity
import random

class Dragon(entity.Entity):
  """Dragon class inherited from Entity class"""
  def basic_attack(self, other):
    dmg = random.randint(3,7)
    other.take_damage(dmg)
    return f"{self.name} smashes you with its tail for {dmg} damage!"

  def special_attack(self, other):
    dmg = random.randint(4,8)
    other.take_damage(dmg)
    return f"{self.name} slashes you with its tail for {dmg} damage!"