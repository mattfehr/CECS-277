import entity
import random

class Goblin(entity.Entity):
  '''
  name - expert goblin name
  max hp - expert goblin max hp
  hp - expert goblin current hp
  '''
  def __init__(self):
    health = random.randint(8,12)
    super().__init__("Mutated Goblin", health)

  def attack(self, entity):
    dmg = random.randint(6,12)
    entity.take_damage(dmg)
    return f"{self._name} hit {entity.name} for {dmg} damage"