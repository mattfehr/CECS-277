import task


class Tasklist:
  #create a task list by reading the file and sort
  def __init__(self):
    file = open("tasklist-1.txt")
    self._tasklist = []
    for current_task in file.readlines():
      desc, date, time = current_task.strip().split(",")
      self._tasklist.append(task.Task(desc, date, time))
    self._tasklist.sort()
    file.close()

  def add_task(self, desc, date, time):
    #create a task and add it to the list and sort
    self._tasklist.append(task.Task(desc, date, time))
    self._tasklist.sort()

  def mark_complete(self):
    #remvove the top task from the task list
    self._tasklist.pop(0)

  def save_file(self):
    #write the contents of the task list into the text file
    file = open("tasklist-1.txt", "w")
    for t in self._tasklist:
      file.write(repr(t) + "\n")
    file.close()

  def get_current_task(self):
    return self._tasklist[0]

  def __iter__(self):
    self._n = -1
    return self

  def __next__(self):
    self._n += 1
    if self._n > len(self._tasklist) - 1:
      raise StopIteration
    else:
      return self._tasklist[self._n]

  def __len__(self):
    return len(self._tasklist)
