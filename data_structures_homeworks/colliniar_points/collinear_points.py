from point import Point
from line_segment import LineSegment
from collections import namedtuple

SlopeAndPoint = namedtuple(
  'SlopeAndPoint', ['slope', 'point']
)


class CollinearPoints:
  def __init__(self, points):
    self.points = points
    self.collenear_line_segments = []

  def __repr__(self):
    return str(self.points)

  def get_slopes_and_points(self, origin):
    slopes_and_points = []
    for point in self.points:
      slopes_and_points.append(
        SlopeAndPoint(origin.slope_to(point), point)
      )

    return slopes_and_points

  # def get_groups_of_four_collinear_points(self):
  #   if len(self.points) < 4:
  #     return

  #   for point in self.points:
  #     get_segments(point)

  # def get_segments(self, point):
  #   slopes_and_points = get_slopes_and_points(point)
  #   slopes_and_points.sort()
  #   entries_so_far = []
  #   for slope_and_point in slopes_and_points:
  #     if len(entries_so_far) < 1:
  #       entries_so_far.append(slope_and_point)
  #     else:

