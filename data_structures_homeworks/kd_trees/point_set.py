from typing import List, Tuple

from point_2d import Point
from rectangle import Rectangle
from line_segment import LineSegment, Color
from kd_tree import Kd_Tree, EmptyNode

import matplotlib.pyplot as plt

class Point_Set:
  def __init__(self):
    self.kd = Kd_Tree()

  def __repl__(self):
    return self.kd

  def is_empty(self):
    return self.kd.is_empty()

  def size(self):
    return self.kd.size()

  def contains(self, point: Point):
    return self.kd.contains()

  def insert(self, point: Point):
    return self.kd.insert(point)

  def draw(self):
    if self.is_empty():
      return

    nodes = [self.kd.root]
    for node in nodes:
      if node.level%2  == 0:
        self.draw_vertical_line(node.point, node.parent)
      else:
        self.draw_horizontal_line(node.point, node.parent)

      node.point.draw()

      if node.left.__class__ != EmptyNode:
        nodes.append(node.left)
      if node.right.__class__ != EmptyNode:
        nodes.append(node.right)

  def draw_vertical_line(self, point, parent):
    top = Point(point.x, 10)
    bottom = Point(point.x, 0)

    if parent is not None:
      if point.y < parent.point.y:
        top.y = parent.point.y
      else:
        bottom.y = parent.point.y
    LineSegment(top, bottom).draw(Color.RED)

  def draw_horizontal_line(self, point, parent):
    top = Point(10, point.y)
    bottom = Point(0, point.y)

    if parent is not None:
      if point.x < parent.point.x:
        top.x = parent.point.x
      else:
        bottom.x = parent.point.x

    LineSegment(top, bottom).draw(Color.BLUE)
