from point_2d import Point
from enum import Enum


class NodeSide(Enum):
  LEFT = "left"
  RIGHT = "right"


class EmptyNode:
  def __init__(self, level: int=0):
    self.level = level

  def __repr__(self):
    return f"(    )"


class Node:
  def __init__(self, point: Point, level: int = 0, parent=None):
    self.point = point
    self.left = EmptyNode(level + 1)
    self.right = EmptyNode(level + 1)
    self.level = level
    self.parent = parent

  def __repr__(self):
    return f"{self.point}"


class Kd_Tree:
  root = EmptyNode()

  def is_empty(self) -> bool:
    return self.root.__class__ == EmptyNode

  def insert(self, point) -> None:
    if self.is_empty():
      self.root = Node(point)
      return

    leaf = self.get_leaf(self.root, point)
    node = Node(point, leaf.level + 1, leaf)
    if self.get_leaf_side(leaf, point) is NodeSide.LEFT:
      leaf.left = node
    else:
      leaf.right = node

  def size(self):
    nodes = [self.root]
    for node in nodes:
      if node.__class__ != EmptyNode:
        nodes.append(node.left)
        nodes.append(node.right)

    return len(list(filter(lambda x: x.__class__ != EmptyNode, nodes)))

  def get_leaf(self, node: Node, point: Point) -> Node:
    if self.get_leaf_side(node, point) is NodeSide.LEFT:
      if node.left.__class__ == EmptyNode:
        return node
      return self.get_leaf(node.left, point)
    else:
      if node.right.__class__ == EmptyNode:
        return node
      return self.get_leaf(node.right, point)

  def get_leaf_side(self, node: Node, point: Point) -> NodeSide:
    if node.level % 2 == 0:
      if point.x < node.point.x:
        return NodeSide.LEFT
      else:
        return NodeSide.RIGHT
    else:
      if point.y < node.point.y:
        return NodeSide.LEFT
      else:
        return NodeSide.RIGHT

  def get_closest_node(self, node: Node, point: Point) -> Node:
    if node.left.__class__ == EmptyNode and node.right.__class__ == EmptyNode:
      return node

    if node.point == point:
      return node

    if self.get_leaf_side(node, point) is NodeSide.LEFT:
      return self.get_closest_node(node.left, point)
    else:
      return self.get_closest_node(node.right, point)

  def contains(self, point: Point) -> bool:
    if self.is_empty():
      return False
    closest_node = self.get_closest_node(self.root, point)
    return closest_node.point == point

  def __repr__(self) -> str:
    nodes = [self.root]
    for node in nodes:
      if node.__class__ != EmptyNode:
        nodes.append(node.left)
        nodes.append(node.right)

    return_string = ""
    level = 0
    for node in nodes:
      if node.level != level:
        return_string += "\n"
        level = node.level
      return_string += f"{node}   "

    return return_string
