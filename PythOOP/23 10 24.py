from math import tan, pi

class shape:
  def __init__(self, shap, nosides, length):
    self.type = shap
    self.nosides = nosides
    self.length = length
    self.area = 0

  def areafinder(self):
    self.area = self.nosides * (self.length ** 2) / (4 * tan(pi / self.nosides))
    if self.area <= 0:
      print("The area is not a real shape")
    else:
      print("Area of the polygon is:", self.area)

hexagon = shape("hexagon", 6, 18)
hexagon.areafinder()
