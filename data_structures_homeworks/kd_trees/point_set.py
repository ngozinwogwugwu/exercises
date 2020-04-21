from typing import List, Tuple

from point_2d import Point, max_value
from rectangle import Rectangle
from line_segment import LineSegment, Color
from kd_tree import Kd_Tree, EmptyNode, Node

import matplotlib.pyplot as plt

class Point_Set:
  def __init__(self):
    self.kd = Kd_Tree()

  def __repl__(self) -> Kd_Tree:
    return self.kd

  def is_empty(self) -> bool:
    return self.kd.is_empty()

  def size(self) -> int:
    return self.kd.size()

  def contains(self, point: Point) -> bool:
    return self.kd.contains()

  def insert(self, point: Point) -> None:
    self.kd.insert(point)

  def draw(self) -> None:
    if self.is_empty():
      return

    nodes = [self.kd.root]
    for node in nodes:
      node.draw()

      if node.left.__class__ != EmptyNode:
        nodes.append(node.left)
      if node.right.__class__ != EmptyNode:
        nodes.append(node.right)

  def draw_range(self, rectangle: Rectangle) -> None:
    rectangle.draw()

    for point in self.range(rectangle, self.kd.root):
      point.draw_special()


  def range(self, rectangle: Rectangle, node: Node) -> List[Point]:
    if not node.rectangle.intersects(rectangle):
      return []

    points = []

    if rectangle.contains(node.point):
      points.append(node.point)

    if node.left.__class__ != EmptyNode:
      points += self.range(rectangle, node.left)
    if node.right.__class__ != EmptyNode:
      points += self.range(rectangle, node.right)

    return points


