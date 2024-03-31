import entity
import random

class Skeleton(entity.Entity):
  '''
  name - expert skeleton name
  max hp - expert skeleton max hp
  hp - expter skeleton current hp
  '''
  def __init__(self):
    health = random.randint(6,10)
    super().__init__("Flaming Zombie", health)

  def attack(self, entity):
    dmg = random.randint(6,10)
    entity.take_damage(dmg)
    return f"{self._name} hit {entity.name} for {dmg} damage"