from typing import List, Tuple

from point_2d import Point, max_value
from rectangle import Rectangle
from line_segment import LineSegment, Color
from kd_tree import Kd_Tree, EmptyNode, Node
from point_set import Point_Set

import matplotlib.pyplot as plt

from random import randrange

def write_to_points_file(filename, num_points):
  points_file = open(filename, 'w')
  points_file.write(f"{num_points}\n")

  for i in range(num_points):
    points_file.write(f"{randrange(max_value)} {randrange(max_value)}\n")
  points_file.close()


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
  ps = Point_Set()
  
  for line in range(num_points):
    [x, y] = points_file.readline().split(' ')
    ps.insert(Point(int(x), int(y)))

  points_file.close()
  return ps

write_to_points_file('input7.txt', 50)

point_set = get_points_from_file('input7.txt')
# print(point_set.kd)
point_set.draw()
min_x = randrange(max_value/2)
max_x = min_x + randrange(max_value/2)
min_y = randrange(max_value/2)
max_y = min_y + randrange(max_value/2)
point_set.draw_range(Rectangle(min_x, max_x, min_y, max_y))
plt.show()
