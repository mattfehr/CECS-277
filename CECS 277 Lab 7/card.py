class Card:
  """
  _rank = an integer property index 0-12 representing the card ranks
  _suit = an integer index 0-3 representing the card suits
  """
  def __init__(self, suit, rank):
    self._rank = rank
    self._suit = suit

  @property
  def rank(self):
    return self._rank

  def __str__(self):
    ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King", "Ace"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    return f"{ranks[self.rank]} of {suits[self._suit]}"

  def __lt__(self, other):
    return self.rank < other.rank