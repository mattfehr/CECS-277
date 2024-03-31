#Names: Matthew Fehr and Tin Nguyen
#Date: 9/25/23
#Description: Program to keep track on upcoming tasks

import task
import tasklist
import check_input

def main_menu():
  #display the options
  choice = check_input.get_int_range(
  """
  1. Display current task
  2. Display all tasks
  3. Mark current task complete
  4. Add new task
  5. Save and quit
  Enter choice: """, 1,5)
  return choice

def get_date():
  #get the assignment due date
  print("Enter due date:")
  month = str(check_input.get_int_range("Enter month: ", 1,12))
  if int(month) < 10:
    month = "0"+month
  day = str(check_input.get_int_range("Enter day: ", 1, 31))
  if int(day) < 10:
    day = "0"+day
  year = str(check_input.get_int_range("Enter year: ", 2000, 3000))
  return f"{month}/{day}/{year}"

def get_time():
  #get the time the assignment is due
  print("Enter time:")
  hour = str(check_input.get_int_range("Enter hour:", 0, 23))
  if int(hour) < 10:
    hour = "0"+hour
  minute = str(check_input.get_int_range("Enter minute:", 0, 59))
  if int(minute) < 10:
    minute = "0"+minute
  return f"{hour}:{minute}"

def main():
  #create the task list
  task_list = tasklist.Tasklist()
  #loop for using the task list
  while True:
    print("-Tasklist")
    print(f"Tasks to complete: {len(task_list)}")
    choice = main_menu()
    
    #display the current 
    if choice == 1:
      print("Current task is: ")
      print(task_list[0])
      
    #display every task
    elif choice == 2:
      if len(task_list) == 0:
        print("There are no tasks")
      else:
        for t in task_list:
          print(t)
          
    #mark the current task complete and display next one
    elif choice == 3:
      if len(task_list) == 0:
        print("There are no more tasks")
      else:
        print("Marking current task as complete:")
        print(task_list[0])
        task_list.mark_complete()
        if len(task_list):
          print("New current task is:")
          print(task_list[0])

    #add a new task to the list
    elif choice == 4:
      desc = input("Enter a task: ")
      date = get_date()
      time = get_time()
      task_list.add_task(desc,date,time)

    #save the changed task list into the file and quit
    else:
      task_list.save_file()
      break 
    print()
      
main()