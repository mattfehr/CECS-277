import entity
import random
import map 


class Hero(entity.Entity):
  '''
  name - hero name
  max hp - hero max hp
  hp - hero current hp
  loc - hero current location
  '''
  def __init__(self, name):
    super().__init__(name, 25)
    self._loc = [0, 0]  #y,x #row, column

  @property
  def loc(self):
    return self._loc

  def attack(self, entity):
    dmg = random.randint(2, 5)
    entity.take_damage(dmg)
    return f"{self._name} attacks a {entity._name} for {dmg} damage"

  def go_north(self):
    map_inst = map.Map()
    #check if the player is at the top
    if self.loc[0] > 0: 
      self._loc[0] -= 1
      return map_inst[self.loc[0]][self.loc[1]]
    else:
      return 'o'

  def go_south(self):
    map_inst = map.Map()
    #check if the player is at the bottom
    if self.loc[0] < len(map_inst) - 1:
      self.loc[0] += 1
      return map_inst[self.loc[0]][self.loc[1]]
    else:
      return 'o'

  def go_east(self):
    map_inst = map.Map()
    #check if the player at the right
    if self.loc[1] < len(map_inst) - 1:
      self.loc[1] += 1
      return map_inst[self.loc[0]][self.loc[1]]
    else:
      return 'o'

  def go_west(self):
    map_inst = map.Map()
    #check if the player is at the left
    if self.loc[1] > 0:
      self.loc[1] -= 1
      return map_inst[self.loc[0]][self.loc[1]]
    else:
      return 'o'
