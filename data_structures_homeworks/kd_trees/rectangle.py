from point_2d import Point_2d
from line_segment import LineSegment


class Rectangle:
  def __init__(self, x_min: float, x_max: float, y_min: float, y_max: float) -> None:
    self.x_min = x_min
    self.x_max = x_max
    self.y_min = y_min
    self.y_max = y_max

    self.top_left = Point_2d(x_min, y_max)
    self.top_right = Point_2d(x_max, y_max)
    self.bottom_left = Point_2d(x_min, y_min)
    self.bottom_right = Point_2d(x_max, y_min)

    self.corners = [
        self.top_left, self.top_right, self.bottom_left, self.bottom_right
    ]

    self.top_segment = LineSegment(self.top_left, self.top_right)
    self.bottom_segment = LineSegment(self.bottom_left, self.bottom_right)
    self.left_segment = LineSegment(self.top_left, self.bottom_left)
    self.right_segment = LineSegment(self.top_right, self.bottom_right)
    self.line_segments = [
        self.top_segment,
        self.bottom_segment,
        self.left_segment,
        self.right_segment
    ]

  def __repr__(self) -> str:
    return f"({self.x_min}, {self.y_min}), ({self.x_max}, {self.y_max})"

  def __eq__(self, other) -> bool:
    return self.x_min == other.x_min and self.x_max == other.x_max and self.y_min == other.y_min and self.y_max == other.y_max

  def contains(self, point: Point_2d) -> bool:
    return point.x <= self.x_max and point.x >= self.x_min and point.y <= self.y_max and point.y >= self.y_min

  def intersects(self, other):
    for self_line in self.line_segments:
      for other_line in other.line_segments:
        if self_line.intersects(other_line):
          return True
    return False

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
