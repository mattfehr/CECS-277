import door
import random


class Locked_Door(door.Door):
  """
  _key_location = a key will be placed randomly into 1 of 3 locations
  _input = class's input
  """
  def __init__(self):
    self._key_location = random.randint(1, 3)
    self._input = 0

  def examine_door(self):
    return "a locked door. Look around for the key."

  def menu_options(self):
    return "1. Look under the mat\n2. Look under the flower pot\n3. Look under the fake rock.\n"

  def get_menu_max(self):
    return 3

  def attempt(self, option):
    #copy user input into class's input
    self._input = option
    if option == 1:
      return "You looked under the mat"
    elif option == 2:
      return "You looked under the flower pot"
    else:
      return "You looked under the fake rock"

  def is_unlocked(self):
    #return true if value is matching and false otherwise
    return self._input == self._key_location

  def clue(self):
    return "Look somewhere else"

  def success(self):
    return "Congrats, you unlocked and opened the locked door"
