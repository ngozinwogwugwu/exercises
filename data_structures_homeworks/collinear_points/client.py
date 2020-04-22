from point import Point
from line_segment import LineSegment
from collinear_points import CollinearPoints
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


def points_x_values(points):
  x_values = []
  for point in points:
    x_values.append(point.x)

  return x_values


def points_y_values(points):
  y_values = []
  for point in points:
    y_values.append(point.y)

  return y_values


def get_points_from_file(filename):
  points_file = open(filename, 'r')
  num_points = int(points_file.readline())

  points = []
  for line in range(num_points):
    [x, y] = points_file.readline().split(' ')
    points.append(Point(int(x), int(y)))

  points_file.close()
  return points


def draw_points(points):
  fig, ax = plt.subplots()
  ax.scatter(points_x_values(points), points_y_values(points))
  ax.grid(True)
  fig.tight_layout()
  plt.show()

def draw_points_with_lines(points):
  col_pts = CollinearPoints(points)

  fig, ax = plt.subplots()
  ax.scatter(points_x_values(points), points_y_values(points))
  ax.grid(True)

  for segment in col_pts.segments():
    ax.add_line(mlines.Line2D(
        [segment.p.x, segment.q.x], [segment.p.y, segment.q.y]))

  fig.tight_layout()
  plt.show()


points = get_points_from_file('input8.txt')
draw_points(points)
draw_points_with_lines(points)
