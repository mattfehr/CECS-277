#Name: Matthew Fehr and Tin Nguyen
#Date: 9/11/2023
#Description: A maze game where the user tries to reach a point from a start

import check_input

#create a 2D list based on the maze text file
def read_maze():
  file = open("maze.txt")
  list2d = []
  for row in file:
      list = []
      for item in row:
        if item != "\n":
          list.append(item)
      list2d.append(list)
  file.close()
  return list2d

#find the starting location of the user
def find_start(maze):
    for row in range(len(maze)):
      for column in range(len(maze[row])):
        if maze[row][column] == "s":
          return [row, column]

#display the maze with the user location as X
def display_maze(maze, loc):
  for row in range(len(maze)):
    for column in range(len(maze[row])):
      if loc == [row, column]:
        print("X", end = ' ')
      else:
        print(maze[row][column], end = ' ')
    print()

def main():
  maze = read_maze()
  user_loc = find_start(maze)
  print("-Maze Solver-")
  win = False
  #loop for displaying the maze and asking for moves
  while win == False:
    display_maze(maze, user_loc)
    print("1. Go North")
    print("2. Go South")
    print("3. Go East")
    print("4. Go West")
    move = check_input.get_int_range("Enter choice: ", 1,4)
    #check user move (repeat for all moves)
    if move == 1:
      #check if there is a wall where the user wants to move
      if maze[user_loc[0]-1][user_loc[1]] == "*":
        print("You cannot move there.")
      else:
        #update the user location if there is no wall
        user_loc[0] -= 1
        
    elif move == 2:
      if maze[user_loc[0]+1][user_loc[1]] == "*":
        print("You cannot move there.")
      else:
        user_loc[0] += 1
        
    elif move == 3:
      if maze[user_loc[0]][user_loc[1]+1] == "*":
        print("You cannot move there.")
      else:
        user_loc[1] += 1
        
    else:
      if maze[user_loc[0]][user_loc[1]-1] == "*":
        print("You cannot move there.")
      else:
        user_loc[1] -= 1
        
    #check if the user won
    if maze[user_loc[0]][user_loc[1]] == "f":
      win = True
      
  display_maze(maze, user_loc)
  print("Congratulations! You solved the maze.")
main()
  