import task

class Tasklist:
  #create a task list by reading the file and sort
  def __init__(self):
    file = open("tasklist.txt")
    self.tasklist = []
    for current_task in file.readlines():
      desc,date,time = current_task.strip().split(",")
      self.tasklist.append(task.Task(desc, date, time))
    self.tasklist.sort()
    file.close()

  def add_task(self, desc, date, time):
    #create a task and add it to the list and sort
    self.tasklist.append(task.Task(desc,date,time))
    self.tasklist.sort()

  def mark_complete(self):
    #remvove the top task from the task list
    self.tasklist.pop(0)

  def save_file(self):
    #write the contents of the task list into the text file
    file = open("tasklist.txt", "w")
    for t in self.tasklist:
      file.write(repr(t)+"\n")
    file.close()

  def __getitem__(self, index):
    return self.tasklist[index]

  def __len__(self):
    return len(self.tasklist)
    

  
    
