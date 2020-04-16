from math import sqrt

class Point_2d:
  def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y

  def __repr__(self) -> str:
    return f"({self.x}, {self.y})"

  def distance_to(self, other_point) -> float:
    return sqrt(self.distance_squared_to(other_point))

  def slope_to(self, other_point):
    y_diff = other_point.y - self.y
    x_diff = other_point.x - self.x

    try:
      return y_diff/x_diff
    except ZeroDivisionError as error:
      if y_diff >= 0:
        return float('inf')
      else:
        return float('-inf')

  def distance_squared_to(self, other_point) -> float:
    y_diff = other_point.y - self.y
    x_diff = other_point.x - self.x

    return y_diff**2 + x_diff**2

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __lt__(self, other):
    if self.y < other.y:
      return True
    if self.y > other.y:
      return False

    if self.x < other.x:
      return True
    return False
