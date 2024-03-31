import player

class Dealer(player.Player):
  def play(self):
    string = "Dealer's Cards:\n" + str(self) + "\n"
    while True:
      score = self.score()
      if score <= 16: #hit if its less than 16
        string += "Dealer Hits!\n"
        self.hit()
      if score > 21: #end if the dealer busts
        string += "Busts!"
        break
      if score >= 17 and score <= 21: #stay if its greater than 16 and not bust
        break
      string += "\nDealer's Cards:\n" + str(self) + "\n"
    return string
      
    