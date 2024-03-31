import plate

class SmallPlate(plate.Plate):
  #has description, area, weight and count of whats on the plate
  def description(self):
    return "Sturdy 10 inch paper plate"

  def area(self):
    return 78

  def weight(self):
    return 32

  def count(self):
    return 0