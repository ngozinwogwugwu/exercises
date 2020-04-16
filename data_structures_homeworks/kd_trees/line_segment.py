from point_2d import Point_2d

infinity = float("inf")

class LinesParallelError(Exception):
  pass

class Line:
  def __init__(self, p: Point_2d, q: Point_2d):
    self.point = p
    self.slope = self.point.slope_to(q)
    self.y_intercept = self.get_y_intercept()

  def __repr__(self):
    return f"{self.slope}x + {self.y_intercept} = y"

  def get_y_intercept(self):
    try:
      if self.slope == infinity:
        return None
      else:
        return (self.point.y - self.point.x) / self.slope
    except ZeroDivisionError as e:
      return self.point.y - self.point.x

  def get_y(self, x):
    if self.slope == infinity:
      raise Exception('no y')

    return (self.slope * x) + self.y_intercept

  def intersects_at(self, other) -> Point_2d:
    if self.slope == other.slope:
      raise LinesParallelError

    elif self.slope == infinity:
      x = self.point.x
      y = other.get_y(x)

    elif other.slope == infinity:
      x = other.point.x
      y = self.get_y(x)

    else:
      x = (other.y_intercept - self.y_intercept) / (self.slope - other.slope)
      y = (self.slope * x) + self.y_intercept

    return Point_2d(x, y)


class LineSegment:
  def __init__(self, p: Point_2d, q: Point_2d):
    self.p = p
    self.q = q
    self.line = Line(p, q)

  def contains(self, point) -> bool:
    if self.line.get_y(point.x) != point.y:
      return False

    return (self.p < point and point < self.q) or (self.q < point and point < self.p)

  def overlaps(self, other) -> bool:
    if self.line.slope == infinity and self.p.x != other.p.x:
      return False

    if self.line.slope != other.line.slope:
      return False

    return self.contains(other.p) or self.contains(other.q)

  def intersects(self, other) -> bool:
    try:
      intersection = self.line.intersects_at(other.line)
    except LinesParallelError as e:
      return self.overlaps(other)

    return self.contains(intersection)

  def __repr__(self):
    return f"({self.p}, {self.q})"
