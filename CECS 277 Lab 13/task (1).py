class Task:
  def __init__(self, desc, date, time):
    #each task has a desciption and due date
    self._description = desc
    self._date = date
    self._time = time

  @property
  def date(self):
    return self._date

  def __str__(self):
    return f"{self._description} - Due: {self._date} at {self._time}"

  def __repr__(self):
    return f"{self._description},{self._date},{self._time}"

  def __lt__(self, other):
    #compare by checking string slices
    if self._date[6:10] == other._date[6:10]:
      if self._date[0:2] == other._date[0:2]:
        if self._date[3:5] == other._date[3:5]:
          if self._time[0:2] == other._time[0:2]:
            if self._time[3:5] == other._time[3:5]:
              return self._description < other._description
            return self._time[3:5] < other._time[3:5]
          return self._time[0:2] < other._time[0:2]
        return self._date[3:5] < other._date[3:5]
      return self._date[0:2] < other._date[0:2]
    return self._date[6:10] < other._date[6:10]
      
    
  