import plate

class LargePlate(plate.Plate):
  #has description, area, weight and count of whats on the plate
  def description(self):
    return "Flimsy 12 inch paper plate"

  def area(self):
    return 113

  def weight(self):
    return 24

  def count(self):
    return 0