import unittest
from point_2d import Point_2d
from rectangle import Rectangle
from line_segment import Line, LineSegment

class TestPoint2d(unittest.TestCase):
    def test_distance_to(self):
      point_1 = Point_2d(0, 0)
      point_2 = Point_2d(3, 4)

      self.assertEqual(point_1.distance_to(point_2), 5.0)

    def test_distance_squared_to(self):
      point_1 = Point_2d(0, 0)
      point_2 = Point_2d(3, 4)
      self.assertEqual(point_1.distance_squared_to(point_2), 25.0)

    def test_equal(self):
      point_1 = Point_2d(0, 0)
      point_2 = Point_2d(0, 0)
      point_3 = Point_2d(3, 4)
      self.assertTrue(point_1 == point_2)
      self.assertFalse(point_1 == point_3)


class TestRectangle(unittest.TestCase):
  def test_contains(self):
    rectangle = Rectangle(-1, 1, -1, 1)
    self.assertTrue(rectangle.contains(Point_2d(0, 0)))
    self.assertFalse(rectangle.contains(Point_2d(10, 0)))

class TestLine(unittest.TestCase):
  def test_intersects_at(self):
    line_1 = Line(Point_2d(0, 0), Point_2d(5, 5))
    line_2 = Line(Point_2d(0, 2), Point_2d(5, 2))
    line_3 = Line(Point_2d(1, 0), Point_2d(1, 5))
    self.assertEqual(line_1.intersects_at(line_2), Point_2d(2, 2))
    self.assertEqual(line_1.intersects_at(line_3), Point_2d(1, 1))
    self.assertEqual(line_2.intersects_at(line_3), Point_2d(1, 2))


class TestLineSegment(unittest.TestCase):
  def test_contains(self):
    segment = LineSegment(Point_2d(0, 0), Point_2d(5, 5))
    self.assertTrue(segment.contains(Point_2d(2, 2)))
    self.assertTrue(segment.contains(Point_2d(1, 1)))
    self.assertFalse(segment.contains(Point_2d(6, 6)))
    self.assertFalse(segment.contains(Point_2d(3, 2)))

  def test_overlaps(self):
    segment_1 = LineSegment(Point_2d(0, 0), Point_2d(5, 5))
    segment_2 = LineSegment(Point_2d(0, 2), Point_2d(5, 2))
    segment_3 = LineSegment(Point_2d(1, 0), Point_2d(1, 5))
    segment_4 = LineSegment(Point_2d(1, 1), Point_2d(2, 2))
    segment_5 = LineSegment(Point_2d(-1, -1), Point_2d(-3, -3))
    segment_6 = LineSegment(Point_2d(0, 1), Point_2d(5, 6))
    self.assertFalse(segment_1.overlaps(segment_2))
    self.assertFalse(segment_1.overlaps(segment_3))
    self.assertFalse(segment_2.overlaps(segment_3))
    self.assertTrue(segment_1.overlaps(segment_4))
    self.assertFalse(segment_1.overlaps(segment_5))
    self.assertFalse(segment_1.overlaps(segment_6))

  def test_intersects(self):
    segment_1 = LineSegment(Point_2d(0, 0), Point_2d(5, 5))
    segment_2 = LineSegment(Point_2d(0, 2), Point_2d(5, 2))
    segment_3 = LineSegment(Point_2d(1, 0), Point_2d(1, 5))
    segment_4 = LineSegment(Point_2d(6, 6), Point_2d(8, 8))
    segment_5 = LineSegment(Point_2d(0, 1), Point_2d(5, 6))
    segment_6 = LineSegment(Point_2d(0, 2), Point_2d(3, 0))

    self.assertTrue(segment_1.intersects(segment_2))
    self.assertTrue(segment_1.intersects(segment_3))
    self.assertTrue(segment_2.intersects(segment_3))
    self.assertFalse(segment_1.intersects(segment_4))
    self.assertFalse(segment_1.intersects(segment_5))
    self.assertFalse(segment_1.intersects(segment_6))


if __name__ == "__main__":
    unittest.main()
