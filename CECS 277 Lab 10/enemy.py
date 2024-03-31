import entity
import random

class Enemy(entity.Entity):
  '''
  name - enemy name
  max hp - enemy max hp
  hp - enemy current hp
  '''
  def __init__(self):
    names = ['Goblin', 'Vampire', 'Ghoul', 'Skeleton', 'Zombie']
    self._name = random.choice(names)
    self._max_hp = random.randint(4, 8)
    self._hp = self._max_hp

  def attack(self, entity):
    dmg = random.randint(1,4)
    entity.take_damage(dmg)
    return f"{self._name} hit {entity.name} for {dmg} damage"
