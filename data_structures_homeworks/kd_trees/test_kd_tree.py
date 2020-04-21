from rectangle import Rectangle
from point_2d import Point, max_value
from kd_tree import Node, Kd_Tree
import unittest


class TestKd_Tree(unittest.TestCase):
  @classmethod
  def setUp(cls):
    cls.point_0 = Point(7, 2)
    cls.point_1 = Point(5, 4)
    cls.point_2 = Point(2, 3)
    cls.point_3 = Point(4, 7)
    cls.point_4 = Point(9, 6)

    cls.kd = Kd_Tree()
    cls.kd.insert(cls.point_0)
    cls.kd.insert(cls.point_1)
    cls.kd.insert(cls.point_2)
    cls.kd.insert(cls.point_3)
    cls.kd.insert(cls.point_4)

  def test_insert(self):
    self.assertEqual(self.kd.root.left.left.point, self.point_2)
    self.assertEqual(self.kd.root.right.point, self.point_4)

  def test_contains(self):
    self.assertTrue(self.kd.contains(Point(4, 7)))
    self.assertFalse(self.kd.contains(Point(5, 7)))

  def test_size(self):
    self.assertEqual(self.kd.size(), 5)

  def test_rectangle(self):
    self.assertEqual(
      self.kd.root.left.right.rectangle,
      Rectangle(0, 7, 4, max_value)
    )


if __name__ == "__main__":
  unittest.main()
