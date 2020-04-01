from point import Point
from line_segment import LineSegment
from collections import namedtuple, defaultdict

class CollinearPoints:
  def __init__(self, points):
    self.points = points
    self.collenear_line_segments = []

  def __repr__(self):
    return str(self.points)


  def segments(self):
    segments = []
    for point in self.points:
      new_segments = self.get_collinear_line_segments_for_single_point(point)
      segments = segments + new_segments

    return segments

  def get_collinear_line_segments_for_single_point(self, origin):
    qualifying_sets = self.get_sets_of_qualifying_points(origin)
    line_segments = []

    for qualifying_set in qualifying_sets:
      qualifying_set.append(origin)
      qualifying_set.sort()

      min_point = qualifying_set[0]
      max_point = qualifying_set[len(qualifying_set)-1]
      line_segments.append(LineSegment(min_point, max_point))

    return line_segments

  def get_sets_of_qualifying_points(self, origin):
    slopes_and_points = defaultdict(list)
    for point in self.points:
      if point is not origin:
        slopes_and_points[origin.slope_to(point)].append(point)

    return list(dict(
          filter(
            lambda item: len(item[1]) > 2,
            slopes_and_points.items()
          )
        ).values())