import entity
import random

class EasyZombie(entity.Entity):
  '''
  name - easyzombie name
  max hp - easyzombie max hp
  hp - easyzombie current hp
  '''
  def __init__(self):
    health = random.randint(4,5)
    super().__init__("Easy Zombie", health)

  def attack(self, entity):
    dmg = random.randint(1,5)
    entity.take_damage(dmg)
    return f"{self._name} hit {entity.name} for {dmg} damage"
    