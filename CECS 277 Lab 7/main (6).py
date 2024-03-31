#Names: Matthew Fehr and Tin Nguyen
#Date: 10/2/2023
#Description: Simplified blackjack game of a player against a dealer

import card
import deck
import player
import dealer
import check_input
import random

def display_winner(pScore, dScore, points):
  #declare the winner based on the dealer and player scores and update the win counter
  if pScore > 21 and dScore > 21:
    print("Tie")
  elif pScore > 21 or pScore < dScore:
    print("Dealer wins")
    points[1] += 1
  elif dScore > 21 or dScore < pScore:
    print("Player wins")
    points[0] += 1
  elif pScore == dScore:
    print("Tie")
  print(f"Player's points: {points[0]}")
  print(f"Dealer's points {points[1]}")

def main():
  #initialize the deck
  the_deck = deck.Deck()
  the_deck.shuffle()
  print("-Blackjack-")
  print()
  points = [0,0]

  #loop for current round
  while True:
    the_player = player.Player(the_deck)
    choice = 1
    
    #loop for players move in round
    while choice != 2:
      print("Player's Cards:")
      print(the_player)
      print("1. Hit")
      print("2. Stay")
      choice = check_input.get_int_range("Enter choice: ",1,2)
      print()
      if choice == 1:
        the_player.hit()
        if the_player.score() > 21:
          print("Player's Cards:")
          print(the_player)
          print("Bust!")
          choice = 2
          
    #create the dealer and play his turn
    print()
    the_dealer = dealer.Dealer(the_deck)
    print(the_dealer.play())
    
    #display the winner
    print()
    display_winner(the_player.score(),the_dealer.score(), points)
    
    #reshuffle the deck if there is low cards 
    if len(the_deck) < 15:
      the_deck = deck.Deck()
      the_deck.shuffle()
      
    #ask the user if he wants to play again
    again = check_input.get_yes_no("Play again? (Y/N): ")
    print()
    if not again:
      break

main()