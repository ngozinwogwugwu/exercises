import matplotlib.pyplot as plt
from enum import Enum
from point_2d import Point
from math import sqrt


def is_infinity(slope):
  return slope == float("inf") or slope == float("-inf")


class LinesParallelError(Exception):
  pass


class Color(Enum):
  BLACK = "k-"
  RED = "r-"
  BLUE = "b-"


class Line:
  def __init__(self, p: Point, q: Point):
    self.point = p
    self.slope = self.point.slope_to(q)
    self.y_intercept = self.get_y_intercept()

  def __repr__(self):
    return f"{self.slope}x + {self.y_intercept} = y"

  def get_y_intercept(self):
    try:
      if is_infinity(self.slope):
        return None
      else:
        # return (self.point.y - self.point.x) / self.slope
        return self.point.y - (self.slope * self.point.x)
    except ZeroDivisionError as e:
      return self.point.y - self.point.x

  def get_y(self, x):
    if is_infinity(self.slope):
      raise Exception('no y')
    return (self.slope * x) + self.y_intercept

  def perpenducular_line_through_point(self, point: Point):
    if is_infinity(self.slope):
      return Line(point, Point(point.x - 1, point.y))
    elif self.slope == 0:
      return Line(point, Point(point.x, point.y - 1))

    # get slope and y intercept of perpendicular line
    slope = -self.slope
    y_intercept = point.y - (slope * point.x)

    # construct another point that would lay on that line
    other_x = point.x - 1
    other_y = (slope * other_x) + y_intercept

    return Line(point, Point(other_x, other_y))

  def closest_position_to_point(self, point: Point) -> Point:
    perpendicular_line = self.perpenducular_line_through_point(point)
    return self.intersects_at(perpendicular_line)

  def intersects_at(self, other) -> Point:
    if self.slope == other.slope:
      raise LinesParallelError

    elif is_infinity(self.slope):
      x = self.point.x
      y = other.get_y(x)

    elif is_infinity(other.slope):
      x = other.point.x
      y = self.get_y(x)

    else:
      x = (other.y_intercept - self.y_intercept) / (self.slope - other.slope)
      y = (self.slope * x) + self.y_intercept

    return Point(x, y)


class LineSegment:
  def __init__(self, p: Point, q: Point):
    self.p = p
    self.q = q
    self.line = Line(p, q)

  def draw(self, color: Color):
    plt.plot(
        [self.p.x, self.q.x],
        [self.p.y, self.q.y],
        color.value,
        linewidth=1
    )

  def contains(self, point) -> bool:
    if is_infinity(self.line.slope):
      if point.x != self.p.x:
        return False
      return (self.p < point and point < self.q) or (self.q < point and point < self.p)

    if self.line.get_y(point.x) != point.y:
      return False

    return (self.p.x < point.x and point.x < self.q.x) or (self.q.x < point.x and point.x < self.p.x)

  def overlaps(self, other) -> bool:
    if is_infinity(self.line.slope) and self.p.x != other.p.x:
      return False

    if self.line.slope != other.line.slope:
      return False

    return self.contains(other.p) or self.contains(other.q)

  def closest_point_to(self, point: Point) -> Point:
    closest = self.line.closest_position_to_point(point)

    if self.contains(closest):
      return closest

    # not vertical
    if min(self.p.x, self.q.x) > closest.x:
      if self.p.x < self.q.x:
        return self.p
      return self.q
    elif max(self.p.x, self.q.x) < closest.x:
      if self.p.x > self.q.x:
        return self.p
      return self.q

    # vertical
    if min(self.p.y, self.q.y) > closest.y:
      if self.p.y < self.q.y:
        return self.p
      return self.q
    elif max(self.p.y, self.q.y) < closest.y:
      if self.p.y > self.q.y:
        return self.p
      return self.q

    raise Exception('not in a case that I thought of')

  def intersects(self, other) -> bool:
    try:
      intersection = self.line.intersects_at(other.line)
    except LinesParallelError as e:
      return self.overlaps(other)

    return self.contains(intersection) and other.contains(intersection)

  def __repr__(self):
    return f"({self.p}, {self.q})"
