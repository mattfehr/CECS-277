import dragon
import random

class FlyingDragon(dragon.Dragon):
  """Special Flying Dragon inherited from Dragon class"""
  def __init__(self, name, max_hp, swoops=5):
    super().__init__(name, max_hp)
    self.swoops = swoops

  #override special attack and only attack if capable
  def special_attack(self, other):
    if self.swoops > 0:
      dmg = random.randint(5,8)
      other.take_damage(dmg)
      self.swoops -= 1
      return f"{self.name} swoops at you for {dmg} damage!"
    return f"{self.name} tries to swoop down to hit you, but failed"

  def __str__(self):
    return super().__str__() + f"\nSwoop attacks remaining: {self.swoops}"

