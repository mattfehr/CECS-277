#Names: Matthew Fehr and Tin Nguyen
#Date: 12/4/23
#Description: Puppy simulator where a puppy can eat, sleep and play

import puppy
import check_input

def main():
  p = puppy.Puppy()
  print("Congratulations on your new puppy!")
  while True:
    #loop of getting actions from user
    choice = check_input.get_int_range("What would you like to do?\n1. Feed the puppy\n2. Play with the puppy\n3. Quit\nEnter choice: ",1,3)
    print()
    if choice == 1:
      #call feed
      print(p.give_food())
    elif choice == 2:
      #call play
      print(p.throw_ball())
    else:
      break
main()