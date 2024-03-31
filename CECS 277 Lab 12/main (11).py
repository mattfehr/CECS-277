#Names: Matthew Fehr and Tin Nguyen
#Date: 11/13/23
#Description: Game where player tries to add as many objects onto a plate as possible without it overflowing

import check_input
import small_plate
import large_plate
import turkey
import stuffing
import potatoes
import green_beans
import pie

def examine_plate(p):
  #print the kind of plate and whats on it
  print(p.description())
  weight = p.weight()
  area = p.area()  
  #if theres too much weight wise or area wise, return True
  if weight <= 0:
    print("Your plate cant hold this much food! The plate collapses.")
    return True
  if area <= 0:
    print("Your plate isn't big enough for this much food! Your food spills over the edge.")
    return True
  #create hints based on weight and area
  if 1 <= weight <= 6:
    print("Sturdiness: Bending")
  elif 7 <= weight <= 12:
    print("Sturdiness: Weak")
  elif weight >= 13:
    print("Sturdiness: Strong")
  if 1 <= area <= 20:
    print("Space available: Tiny bit")
  elif 21 <= area <= 40:
    print("Space available: Some")
  elif area >= 41:
    print("Space available: Plenty")
  return False

def main():
  print("""
- Thanksgiving Dinner -
Serve yourself as much food as you
like from the buffet, but make sure
that your plate will hold without
spilling everywhere!
""")
  
  #choose between small plate or large plate
  plate_choice = check_input.get_int_range("Choose a plate:\n1. Small Sturdy Plate\n2. Large Flimsy Plate\n",1,2)
  if plate_choice == 1:
    p = small_plate.SmallPlate()
  else:
    p = large_plate.LargePlate()
    
  while True:
    #loop for choosing what to add to the plate
    choice = check_input.get_int_range("""
1. Turkey
2. Stuffing
3. Potatoes
4. Green Beans
5. Pie
6. Quit
""", 1,6)
    
    #add to the plate based on choice
    if choice == 1:
      p = turkey.Turkey(p)
    elif choice == 2:
      p = stuffing.Stuffing(p)
    elif choice == 3:
      p = potatoes.Potatoes(p)
    elif choice == 4:
      p = green_beans.GreenBeans(p)
    elif choice == 5:
      p = pie.Pie(p)
    else:
      #if the user quits, examine plate and say how much weight and area they could have used and then quit
      print()
      print(p.description())
      print(f"Good job! You made it to the table with {p.count()} items.")
      print(f"There was still {p.area()} square inches left on your plate.")
      print(f"Your plate could have held {p.weight()} more ounces of food.")
      print("Don't worry, you can always go back for more. Happy Thanksgiving!")
      break
      
    #examine plate after each move, if the weight or area is over, quit
    print()
    res = examine_plate(p)
    if res:
      break
      
main()