import check_input
import random
#Name Tin Nguyen and Matthew Fehr
#Date 8/28/23
#Dec A queen guessing game where you can bet money


def get_users_bet(money):
  #Ask the user for a bet, check the input, then return the integer
  print(f"You have ${money}.")
  bet = check_input.get_int_range("How much you wanna bet? ", 1, money)
  return bet

def get_users_choice():
  #display the card choices, get the users guess, check the input, then return the integer
  print("""
    +-----+ +-----+ +-----+
    |     | |     | |     |
    |  1  | |  2  | |  3  |
    |     | |     | |     |
    +-----+ +-----+ +-----+
    """)
  guess = check_input.get_int_range("Find the queen: ", 1, 3)
  return guess
  

def display_queen_loc(queen_loc):
  #display where the queens location
  if queen_loc == 1:
    print("""
    +-----+ +-----+ +-----+
    |     | |     | |     |
    |  Q  | |  K  | |  K  |
    |     | |     | |     |
    +-----+ +-----+ +-----+
    """)
  elif queen_loc == 2:
    print("""
    +-----+ +-----+ +-----+
    |     | |     | |     |
    |  K  | |  Q  | |  K  |
    |     | |     | |     |
    +-----+ +-----+ +-----+
    """)
  else:
    print("""
    +-----+ +-----+ +-----+
    |     | |     | |     |
    |  K  | |  K  | |  Q  |
    |     | |     | |     |
    +-----+ +-----+ +-----+
    """)

def main():
  print("-Three card Monte-\n Find the queen to double your bet!")
  user_money = 100
  
  cont = 0
  while cont != 1:
    bet = get_users_bet(user_money) #initialize user's bet value
    queen_loc = random.randint(1,3) #randomize queen location
    guess = get_users_choice()      #initialize user's guess
    
    display_queen_loc(queen_loc)    
    if queen_loc != guess:          #if you guess wrong
      print("Sorry... you lose.")
      user_money -= bet
    elif queen_loc == guess:        #if you guess correctly
      print("You got lucky this time...")
      user_money += bet * 2
    
    #check to end the game
    if user_money == 0: 
      print("You're out of money. Beat it loser!")
      cont = 1
    else:  
      play_again = check_input.get_yes_no("Play again? (Y/N): ")
      if play_again == False:
        cont = 1
main()