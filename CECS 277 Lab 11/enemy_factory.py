import abc

class EnemyFactory(abc.ABC):
  #factory interface
  @abc.abstractmethod
  def create_random_enemy(self):
    pass

