import plate_decorator

class GreenBeans(plate_decorator.PlateDecorator):
  #calls super to call self._plate, which is what it is layered on top of
  def description(self):
    return super().description() + " and Green beans"

  def area(self):
    return super().area() - 20

  def weight(self):
    return super().weight() - 3
    
  def count(self):
    return super().count() + 1