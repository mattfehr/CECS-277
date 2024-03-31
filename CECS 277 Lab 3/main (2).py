#Name: Tin Nguyen and Matthew Fehr
#Date: 9/6/23
#Description: Two player Ship, Captain and Crew dice game 

import check_input
import random 

#create a random list of dice values
def roll_dice(dice):
  for i in range(len(dice)):
    dice[i] = random.randint(1,6)
  dice.sort(reverse=True)

#display the dice values for keep and rolls
def display_dice(name, dice):
  dices = ' '.join(str(x) for x in dice)
  print(f"{name} = {dices}")

#determine and display the winners based on scores
def find_winner(player_points):
  print("Score:")
  print(f"Player #1 = {player_points[0]}")
  print(f"Player #2 = {player_points[1]}")
  if player_points[0] > player_points[1]:
    print("Player #1 won!")
  elif player_points[0] < player_points[1]:
    print("Player #2 won!")
  else:
    print("It's a tie!")

def main():
  print("- Ship, Captain, and Crew! –")
  player_points = [0, 0]
  #loop for two players
  for player in range(2):
    keep = []
    roll = [0, 0, 0, 0, 0]
    print()
    print(f"Player {player+1}'s Turn:")
    #loop for three possible rolls
    for roll_number in range(3):
      roll_dice(roll)
      display_dice("Roll", roll)
      #check for ship, add to keep and remove dice
      if 6 in roll and 6 not in keep:
        print("Yo ho ho! Ye secured a ship!")
        keep.append(6)
        roll.remove(6)
      #check for captain, add to keep and remove dice
      if 5 in roll and 6 in keep and 5 not in keep:
        print("Shiver me timbers! A Capt’n!")
        keep.append(5)
        roll.remove(5)
      #check for crew, add to keep and remove dice
      if 4 in roll and 5 in keep and 4 not in keep:
        print("Ye bribed a crew with Grog!")
        keep.append(4)
        roll.remove(4)
      display_dice("Keep", keep)
      #determine cargo and add to points when all numbers are in keeps
      if 4 in keep:
        cargo = ' '.join(str(x) for x in roll)
        player_points[player] = sum(roll)
        print(f"Cargo = {cargo}")
        print("Your cargo points are:", player_points[player])
      print()
      #Check if they want to continue rolling
      if roll_number < 2:
        play_again = check_input.get_yes_no("Roll again? ")
        if play_again == False:
          break
    print(f"Player #{player+1} points = {player_points[player]}")
  print()
  find_winner(player_points)
    
main()
