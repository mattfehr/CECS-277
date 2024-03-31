#Names: Matthew Fehr and Tin Nguyen
#Date: 11/6/23
#Description: Game where hero moves throughout different maps fighting monsters

import map
import hero
import exp_factory
import beg_factory
import check_input
import random

def main():
  #create the hero and the map
  hero_name = input("What is your name, traveler? ")
  player = hero.Hero(hero_name)
  map_instance = map.Map()
  room = [0,0]

  #set the difficulty of the game
  difficulty = check_input.get_int_range("Difficulty:\n1. Beginner\n2. Expert\n",1,2)
  if difficulty == 1:
    factory = beg_factory.BeginnerFactory()
  else:
    factory = exp_factory.ExpertFactory()
  map_counter = 1

  #loop to play the game
  while True:
    #display the player status, update and show the map
    print(player)
    print(map_instance.show_map(player.loc))
    map_instance.reveal(player.loc)

    #get the users choice for movement
    choice = check_input.get_int_range("""1. Go North
2. Go South
3. Go East
4. Go West
5. Quit
Enter choice: """,1,5)
    if choice == 1:
      room = player.go_north()
    elif choice == 2:
      room = player.go_south()
    elif choice == 3:
      room = player.go_east()
    elif choice == 4:
      room = player.go_west()
    elif choice == 5:
      #end the game if they quit
      print("You quit the game")
      break

    #if the selected direction is out of bounds
    if room == "o":
      print("You cannot go that way...")

    #if the room has a monster, give option to fight or run
    elif room == "m":
      #create a random monster with the difficulties factory
      monster = factory.create_random_enemy()
      print(f"You encounter a {monster}")
      print()
      while True:
        hero_choice = check_input.get_int_range(f"1. Attack {monster.name}\n2. Run Away\nEnter Choice: ", 1,2)
        if hero_choice == 1:
          #attack the monster
          print(player.attack(monster))
          if monster.hp <= 0:
            #break out of the fight if the monster dies
            print(f"You have slain the {monster.name}")
            map_instance.remove_at_loc(player.loc)
            break
          else:
            #if the monster doesnt die, attack the player and break out of the fight if the player dies
            print(monster.attack(player))
            if player.hp <= 0:
              break
        else:
          #if the player runs away, choose a random direction to go, reveal the location but dont start any encounters
          print("You ran away!")
          directions = [player.go_north, player.go_south, player.go_west, player.go_east]
          map_instance.reveal(player.loc)
          random_direction = random.choice(directions)
          while random_direction() == "o":
              random_direction = random.choice(directions)
          break

    #state if the room is empty
    elif room == "n":
      print("There is nothing here...")

    #state if the player returned to the start
    elif room == "s":
      print("You are back at the entrance of the dungeon")

    #if the player finds a health potion, return health to full
    elif room == "i":
      print("You found a Health Potion! You drink it to restore your health.")
      player.heal()
      map_instance.remove_at_loc(player.loc)

    #if the player finds the finish, go to the next room by loading the next map
    elif room == 'f':
      print("Congratulations! You found the stairs to the next floor of the dungeon.")
      #loop the maps 1-->2-->3-->1
      map_counter += 1
      if map_counter == 4:
        map_counter = 1
      map_instance.load_map(map_counter)

    #if the player died, end the game
    if player.hp <= 0:
      print("You died.")
      break
            
main()