import enemy_factory
import random
import zombie
import skeleton
import goblin

class ExpertFactory(enemy_factory.EnemyFactory):
  #construct a random expert enemy
  def create_random_enemy(self):
    expert_enemies = ["Zombie", "Skeleton", "Goblin"]
    name = random.choice(expert_enemies)
    if name == "Zombie":
      return zombie.Zombie()
    elif name == "Skeleton":
      return skeleton.Skeleton()
    else:
      return goblin.Goblin()