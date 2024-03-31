class rectangle:
  """
  Represents a rectangle on the coordinate plane.
    Attributes:
    x (int): location x of the rectangle.
    y (int): location y of the rectangle.
    width (int): width of the rectangle.
    height (int): height of the rectangle.
  """
  def __init__(self, w, h):
    self.x = 0
    self.y = 0
    self.width = w
    self.height = h

  def get_coords(self):
    #gives x and y location of rectangle
    return [self.x, self.y]

  def get_dimensions(self):
    #gives the wdith and height of rectangle
    return [self.width, self.height]

  #movement functions by updating the x and y coordinates
  def move_up(self):
    self.y -= 1

  def move_down(self):
    self.y += 1

  def move_left(self):
    self.x -= 1

  def move_right(self):
    self.x += 1
    
  