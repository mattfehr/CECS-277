class Task:
  def __init__(self, desc, date, time):
    #each task has a desciption and due date
    self.description = desc
    self.date = date
    self.time = time

  def __str__(self):
    return f"{self.description} - Due: {self.date} at {self.time}"

  def __repr__(self):
    return f"{self.description},{self.date},{self.time}"

  def __lt__(self, other):
    #compare by checking string slices
    if self.date[6:10] == other.date[6:10]:
      if self.date[0:2] == other.date[0:2]:
        if self.date[3:5] == other.date[3:5]:
          if self.time[0:2] == other.time[0:2]:
            if self.time[3:5] == other.time[3:5]:
              return self.description < other.description
            return self.time[3:5] < other.time[3:5]
          return self.time[0:2] < other.time[0:2]
        return self.date[3:5] < other.date[3:5]
      return self.date[0:2] < other.date[0:2]
    return self.date[6:10] < other.date[6:10]
      
    
  