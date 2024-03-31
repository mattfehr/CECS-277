import plate_decorator

class Potatoes(plate_decorator.PlateDecorator):
  #calls super to call self._plate, which is what it is layered on top of
  def description(self):
    return super().description() + " and Potatoes"

  def area(self):
    return super().area() - 18

  def weight(self):
    return super().weight() - 6

  def count(self):
    return super().count() + 1