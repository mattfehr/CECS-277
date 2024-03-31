import abc

class Entity(abc.ABC):
  """
  _name = entity's name
  _hp = entity's current HP
  _max_hp = entity's starting HP
  """
  def __init__(self, name, max_hp):
    self._name = name
    self._max_hp = max_hp
    self._hp = max_hp

  @property
  def name(self):
    return self._name

  @property 
  def hp(self):
    return self._hp

  @hp.setter
  def hp(self, hp):
    self._hp = hp

  def take_damage(self, dmg):
    self.hp -= dmg
    if self.hp < 0:
      self.hp = 0
      
  def __str__(self):
    return f"{self.name}: {self.hp}/{self._max_hp}"

  @abc.abstractmethod
  def basic_attack(self, other):
    pass

  @abc.abstractmethod
  def special_attack(self, other):
    pass



  
    
    
    
    