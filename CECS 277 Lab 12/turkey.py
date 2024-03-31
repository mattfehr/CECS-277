import plate_decorator

class Turkey(plate_decorator.PlateDecorator):
  #calls super to call self._plate, which is what it is layered on top of
  def description(self):
    return super().description() + " and Turkey"

  def area(self):
    return super().area() - 15

  def weight(self):
    return super().weight() - 4

  def count(self):
    return super().count() + 1