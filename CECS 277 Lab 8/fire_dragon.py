import dragon
import random

class FireDragon(dragon.Dragon):
  """Special Fire Dragon inherited from Dragon class"""
  def __init__(self, name, max_hp, f_shots=3):
    super().__init__(name, max_hp)
    self.fire_shots = f_shots

  def special_attack(self, other):
    #override special attack and only attack if capable
    if self.fire_shots > 0:
      dmg = random.randint(5,9)
      other.take_damage(dmg)
      self.fire_shots -= 1
      return f"{self.name} engulfs you in flames for {dmg} damage!"
    return f"{self.name} tries to split fire at you but is all out of fire shots"

  def __str__(self):
    return super().__str__() + f"\nFire shots remaining: {self.fire_shots}"

