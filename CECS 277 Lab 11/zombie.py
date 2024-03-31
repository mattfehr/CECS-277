import entity
import random

class Zombie(entity.Entity):
  '''
  name - expert zombie name
  max hp - expert zombie max hp
  hp - expert zombie current hp
  '''
  def __init__(self):
    health = random.randint(8,10)
    super().__init__("Titan Zombie", health)

  def attack(self, entity):
    dmg = random.randint(5,12)
    entity.take_damage(dmg)
    return f"{self._name} hit {entity.name} for {dmg} damage"