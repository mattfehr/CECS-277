#Names: Matthew Fehr and Tin Nguyen
#Date: 10/16/23
#Description: Escape room game where player has to unlock three doors by guessing numbers

import locked_door
import check_input
import basic_door
import combo_door
import random
import door

def open_door(door):
  print(f"You encounter {door.examine_door()}")
  while True:
    #continuously get users selection until the door opens
    selection = check_input.get_int_range(door.menu_options(), 1,
                                          door.get_menu_max())
    #try to open the door with the selection and end loop if correct, or else display a clue
    print(door.attempt(selection))
    if door.is_unlocked():
      print(door.success())
      break
    else:
      print(door.clue())

def main():
  print("Welcome to the Escape Room. You must unlock 3 doors to escape...")
  print()

  #A loop that loops 3 times and randomize the values of lock each loop
  for i in range(3):
    #instantiaze the doors
    doors = [
        basic_door.Basic_Door(),
        locked_door.Locked_Door(),
        combo_door.Combo_door()
    ]
    #select the kind of door ranomly
    random_door = random.randint(0, 2)
    open_door(doors[random_door])
    print()
  #exit loop and end game if all three doors are completed
  print("Congratulations, you escaped . . . this time")
  
main()
