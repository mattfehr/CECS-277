import card
import random

class Deck:
  """
  _cards - a list of Card objects that are in the deck
  """
  def __init__(self):
    self._cards = []
    for suit in range(4):
      for rank in range(13):
        self._cards.append(card.Card(suit, rank))
    
  def shuffle(self):
    random.shuffle(self._cards)

  def draw_card(self):
    return self._cards.pop(0)

  def __len__(self):
    return len(self._cards)