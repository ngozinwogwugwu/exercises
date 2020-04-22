class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"({self.x}, {self.y})"

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

  def __lt__(self, other):
    if self.y < other.y:
      return True
    if self.y > other.y:
      return False

    if self.x < other.x:
      return True
    return False
