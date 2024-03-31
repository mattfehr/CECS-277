import card
import deck

class Player:
  """
  _deck = a reference to the deck of cards for both players
  _hand = a list of cards the player is currently holding
  """
  def __init__(self, deck):
    self._deck = deck
    self._hand = []
    self._hand.append(self._deck.draw_card())
    self._hand.append(self._deck.draw_card())
    self._hand.sort()

  def hit(self):
    self._hand.append(self._deck.draw_card())
    self._hand.sort()

  def score(self):
    #add to score using index and the list of face values
    values = [2,3,4,5,6,7,8,9,10,10,10,10,11,1]
    score = 0
    for curr_card in self._hand:
      if curr_card.rank < 8:
        score += values[curr_card.rank]
      elif 8 <= curr_card.rank <= 11:
        score += 10
      else:
        if score < 22:
          score += 11
        else: #ace is only +1 if the score is above 21
          score += 1
    return score
         
  def __str__(self):
    string = ""
    for c in self._hand:
      string += str(c) + "\n"
    string += f"Score = {self.score()}"
    return string