import plate_decorator

class Pie(plate_decorator.PlateDecorator):
  #calls super to call self._plate, which is what it is layered on top of
  def description(self):
    return super().description() + " and Pie"

  def area(self):
    return super().area() - 19

  def weight(self):
    return super().weight() - 8

  def count(self):
    return super().count() + 1