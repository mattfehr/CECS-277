import door
import random


class Combo_door(door.Door):
  """
  _correct_value = a random int value for the lock
  _input = class's input
  """
  def __init__(self):
    self._correct_value = random.randint(1, 10)
    self._input = 0

  def examine_door(self):
    return "a door with a combination lock. You can spin the dial to a number 1-10"

  def menu_options(self):
    return "Enter #1-10: "

  def get_menu_max(self):
    return 10

  def attempt(self, option):
    #copy user's input into class's input
    self._input = option
    return f"You turn the dial to . . . {option}"

  def is_unlocked(self):
    #return true if value is matching and false otherwise
    return self._input == self._correct_value

  def clue(self):
    if self._input < self._correct_value:
      return "Try a higher number."
    else:
      return "Try  a lower number"

  def success(self):
    return "You found the correct value and opened the door."
