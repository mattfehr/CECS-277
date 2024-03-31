import enemy_factory
import random
import easy_zombie
import easy_skeleton
import easy_goblin

class BeginnerFactory(enemy_factory.EnemyFactory):
  #construct a random beginner enemy
  def create_random_enemy(self):
    easy_enemies = ["EasyZombie", "EasySkeleton", "EasyGoblin"]
    name = random.choice(easy_enemies)
    if name == "EasyZombie":
      return easy_zombie.EasyZombie() 
    elif name == "EasySkeleton":
      return easy_skeleton.EasySkeleton()
    else:
      return easy_goblin.EasyGoblin()
    