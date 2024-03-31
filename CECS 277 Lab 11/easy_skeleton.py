import entity
import random

class EasySkeleton(entity.Entity):
  '''
  name - easy skeleton name
  max hp - easy skeleton max hp
  hp - easy skeleton current hp
  '''
  def __init__(self):
    health = random.randint(3,4)
    super().__init__("Easy Skeleton", health)

  def attack(self, entity):
    dmg = random.randint(1,4)
    entity.take_damage(dmg)
    return f"{self._name} hit {entity.name} for {dmg} damage"