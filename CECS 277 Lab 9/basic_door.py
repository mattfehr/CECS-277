import door
import random


class Basic_Door(door.Door):
  """
  _state = randomize Push or Pull
  _input = class's input 
  """
  def __init__(self):
    self._state = random.randint(1, 2)
    self._input = 0

  def examine_door(self):
    return "a basic door, you can either push it or pull it to open"

  def menu_options(self):
    return "1. Push\n2. Pull\n"

  def get_menu_max(self):
    return 2

  def attempt(self, option):
    #copy user input into class's input
    self._input = option 
    if option == 1:
      return "You push the door"
    else:
      return "You pull the door"

  def is_unlocked(self):
    #return true if value is matching and false otherwise
    return self._state == self._input 

  def clue(self):
    return "Try the other way."

  def success(self):
    return "Congratulations, you opened the door."
