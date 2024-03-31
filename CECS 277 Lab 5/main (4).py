#Name: Matthew Fehr and Tin Nguyen
#Date: 9/18/23
#Description: A program where a user can create and move a rectangle around a grid

import rectangle
import check_input

#Function to display the matrix as a grid
def display_grid(grid):
  for row in range(len(grid)):
    for column in range(len(grid[row])):
      print(grid[row][column], end = " ")
    print()

#Reset the grid to default
def reset_grid(grid):
  for row in range(len(grid)):
    for column in range(len(grid[row])):
      grid[row][column] = "."

#Place the rectangle on the grid and change the matrix
def place_rect(grid, rect):
  x = rect.get_coords()[0]
  y = rect.get_coords()[1]
  w = rect.get_dimensions()[0]
  h = rect.get_dimensions()[1]
  for i in range(h):
    for j in range(w):
      grid[y][x] = "*"
      x += 1
    x = rect.get_coords()[0]
    y += 1
  
def main():
  #create the 20 by 20 grid/matrix
  grid = []
  for i in range(20):
    list = []
    for j in range(20):
      list.append(".")
    grid.append(list)

  #prompt the user for rectangle arguments and create the rectangle
  width = check_input.get_int_range("Enter rectangle width (1-5): ", 1,5)
  height = check_input.get_int_range("Enter rectangle height (1-5): ", 1,5)
  print()
  rect = rectangle.rectangle(width, height)
  place_rect(grid, rect)
  display_grid(grid)

  #loop to move the rectangle until the user quits
  while True:
    print()
    response = check_input.get_int_range(
    """
    Enter Direction:
    1. Up
    2. Down
    3. Left
    4. Right
    5. Quit
    """,1,5)
    #check if the user can move up based on the y coordinate, move if it can
    if response == 1:
      if rect.get_coords()[1] == 0:
        print("Can't move there")
      else:
        rect.move_up()
    #check if it can move down based on y coordinate and the height, move if it can
    elif response == 2:
      if rect.get_coords()[1] + rect.get_dimensions()[1] >= 20:
        print("Can't move there")
      else:
        rect.move_down()
    #check if it can move left based on the x coordinate, move if it can
    elif response == 3:
      if rect.get_coords()[0] == 0:
        print("Can't move there")
      else:
        rect.move_left()
    #check if it can move right based on the x coordinate and width, move if it can
    elif response == 4:
      if rect.get_coords()[0] + rect.get_dimensions()[0] >= 20:
        print("Can't move there")
      else:
        rect.move_right()
    #exit the loop if the user quits
    else:
      break
    #reset the grid, place the rectangle in the matrix, then display the matrix as a grid each iteration
    reset_grid(grid)
    place_rect(grid, rect)
    display_grid(grid)
    
main()