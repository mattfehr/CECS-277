import entity
import random

class EasyGoblin(entity.Entity):
  '''
  name - easy goblin name
  max hp - easy goblin max hp
  hp - easy goblin current hp
  '''
  def __init__(self):
    health = random.randint(4,6)
    super().__init__("Easy Zombie", health)

  def attack(self, entity):
    dmg = random.randint(2,5)
    entity.take_damage(dmg)
    return f"{self._name} hit {entity.name} for {dmg} damage"