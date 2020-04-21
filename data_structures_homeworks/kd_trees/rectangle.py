import matplotlib.pyplot as plt
from point_2d import Point
from line_segment import Color, LineSegment


class Rectangle:
  def __init__(self, x_min: float, x_max: float, y_min: float, y_max: float) -> None:
    self.x_min = x_min
    self.x_max = x_max
    self.y_min = y_min
    self.y_max = y_max

    self.top_left = Point(x_min, y_max)
    self.top_right = Point(x_max, y_max)
    self.bottom_left = Point(x_min, y_min)
    self.bottom_right = Point(x_max, y_min)

    self.line_segments = [
        LineSegment(self.top_left, self.top_right),
        LineSegment(self.bottom_left, self.bottom_right),
        LineSegment(self.top_left, self.bottom_left),
        LineSegment(self.top_right, self.bottom_right),
    ]

  def __repr__(self) -> str:
    return f"({self.x_min}, {self.y_min}), ({self.x_max}, {self.y_max})"

  def __eq__(self, other) -> bool:
    return self.x_min == other.x_min and self.x_max == other.x_max and self.y_min == other.y_min and self.y_max == other.y_max

  def draw(self):
    for segment in self.line_segments:
      segment.draw(Color.BLACK)

  def contains(self, point: Point) -> bool:
    return point.x <= self.x_max and point.x >= self.x_min and point.y <= self.y_max and point.y >= self.y_min

  def intersects(self, other):
    for self_line in self.line_segments:
      for other_line in other.line_segments:
        if self_line.intersects(other_line):
          return True
    return other.x_max <= self.x_max and other.x_min >= self.x_min and other.y_max <= self.y_max and other.y_min >= self.y_min

  def distance_squared_to(self, point):
    return self.distance_to(point)**2

  def distance_to(self, point):
    if self.contains(point):
      return 0

    shortest_distance = float("inf")
    for segment in self.line_segments:
      closest_point = segment.closest_point_to(point)
      if closest_point.distance_to(point) < shortest_distance:
        shortest_distance = closest_point.distance_to(point)

    return shortest_distance
