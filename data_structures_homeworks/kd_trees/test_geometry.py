import unittest
from point_2d import Point
from rectangle import Rectangle
from line_segment import Line, LineSegment


class TestPoint2d(unittest.TestCase):
  def test_distance_to(self):
    point_1 = Point(0, 0)
    point_2 = Point(3, 4)

    self.assertEqual(point_1.distance_to(point_2), 5.0)

  def test_distance_squared_to(self):
    point_1 = Point(0, 0)
    point_2 = Point(3, 4)
    self.assertEqual(point_1.distance_squared_to(point_2), 25.0)

  def test_equal(self):
    point_1 = Point(0, 0)
    point_2 = Point(0, 0)
    point_3 = Point(3, 4)
    self.assertTrue(point_1 == point_2)
    self.assertFalse(point_1 == point_3)


class TestRectangle(unittest.TestCase):
  def test_contains(self):
    rectangle = Rectangle(-1, 1, -1, 1)
    self.assertTrue(rectangle.contains(Point(0, 0)))
    self.assertFalse(rectangle.contains(Point(10, 0)))

  def test_intersects(self):
    rectangle_1 = Rectangle(0, 3, 0, 6)
    rectangle_2 = Rectangle(2, 6, 1, 4)
    rectangle_3 = Rectangle(1, 5, 5, 8)
    rectangle_4 = Rectangle(1, 2, 1, 3)

    self.assertTrue(rectangle_1.intersects(rectangle_2))
    self.assertTrue(rectangle_1.intersects(rectangle_3))
    self.assertFalse(rectangle_1.intersects(rectangle_4))
    self.assertFalse(rectangle_2.intersects(rectangle_3))

  def test_distance_to(self):
    rectangle = Rectangle(0, 3, 0, 3)
    self.assertEqual(rectangle.distance_to(Point(1, 5)), 2)
    self.assertEqual(rectangle.distance_to(Point(4, 2)), 1)
    self.assertEqual(rectangle.distance_to(Point(1, 2)), 0)    


class TestLine(unittest.TestCase):
  def test_intersects_at(self):
    line_1 = Line(Point(0, 0), Point(5, 5))
    line_2 = Line(Point(0, 2), Point(5, 2))
    line_3 = Line(Point(1, 0), Point(1, 5))
    self.assertEqual(line_1.intersects_at(line_2), Point(2, 2))
    self.assertEqual(line_1.intersects_at(line_3), Point(1, 1))
    self.assertEqual(line_2.intersects_at(line_3), Point(1, 2))

  def test_closest_position_to_point(self):
    line_1 = Line(Point(0, 0), Point(5, 5))
    self.assertEqual(
      line_1.closest_position_to_point(Point(0, 5)),
      Point(2.5, 2.5)
    )
    self.assertEqual(
      line_1.closest_position_to_point(Point(5, 5)),
      Point(5, 5)
    )



class TestLineSegment(unittest.TestCase):
  def test_contains(self):
    segment = LineSegment(Point(0, 0), Point(5, 5))
    self.assertTrue(segment.contains(Point(2, 2)))
    self.assertTrue(segment.contains(Point(1, 1)))
    self.assertFalse(segment.contains(Point(6, 6)))
    self.assertFalse(segment.contains(Point(3, 2)))

  def test_overlaps(self):
    segment_1 = LineSegment(Point(0, 0), Point(5, 5))
    segment_2 = LineSegment(Point(0, 2), Point(5, 2))
    segment_3 = LineSegment(Point(1, 0), Point(1, 5))
    segment_4 = LineSegment(Point(1, 1), Point(2, 2))
    segment_5 = LineSegment(Point(-1, -1), Point(-3, -3))
    segment_6 = LineSegment(Point(0, 1), Point(5, 6))
    self.assertFalse(segment_1.overlaps(segment_2))
    self.assertFalse(segment_1.overlaps(segment_3))
    self.assertFalse(segment_2.overlaps(segment_3))
    self.assertTrue(segment_1.overlaps(segment_4))
    self.assertFalse(segment_1.overlaps(segment_5))
    self.assertFalse(segment_1.overlaps(segment_6))

  def test_intersects(self):
    segment_1 = LineSegment(Point(0, 0), Point(5, 5))
    segment_2 = LineSegment(Point(0, 2), Point(5, 2))
    segment_3 = LineSegment(Point(1, 0), Point(1, 5))
    segment_4 = LineSegment(Point(6, 6), Point(8, 8))
    segment_5 = LineSegment(Point(0, 1), Point(5, 6))
    segment_6 = LineSegment(Point(0, 2), Point(3, 0))

    self.assertTrue(segment_1.intersects(segment_2))
    self.assertTrue(segment_1.intersects(segment_3))
    self.assertTrue(segment_2.intersects(segment_3))
    self.assertFalse(segment_1.intersects(segment_4))
    self.assertFalse(segment_1.intersects(segment_5))
    self.assertFalse(segment_1.intersects(segment_6))

    segment_7 = LineSegment(Point(3, 6), Point(3, 0))
    segment_8 = LineSegment(Point(2, 4), Point(6, 4))
    self.assertTrue(segment_7.intersects(segment_8))

    segment_9 = LineSegment(Point(0, 6), Point(3, 6))
    segment_10 = LineSegment(Point(1, 2), Point(1, 1))
    self.assertFalse(segment_9.intersects(segment_10))

  def test_closest_point_to(self):
    segment_1 = LineSegment(Point(0, 0), Point(5, 5))
    self.assertEqual(
      segment_1.closest_point_to(Point(1, 1)),
      Point(1, 1)
    )
    self.assertEqual(
      segment_1.closest_point_to(Point(0, 5)),
      Point(2.5, 2.5)
    )
    self.assertEqual(
      segment_1.closest_point_to(Point(6, 6)),
      Point(5, 5)
    )
    self.assertEqual(
      segment_1.closest_point_to(Point(-1, -6)),
      Point(0, 0)
    )

    segment_2 = LineSegment(Point(0, 0), Point(5, 0))
    self.assertEqual(
      segment_2.closest_point_to(Point(-1, 0)),
      Point(0, 0)
    )
    self.assertEqual(
      segment_2.closest_point_to(Point(-1, 60)),
      Point(0, 0)
    )
    self.assertEqual(
      segment_2.closest_point_to(Point(3, 60)),
      Point(3, 0)
    )
    self.assertEqual(
      segment_2.closest_point_to(Point(33, -60)),
      Point(5, 0)
    )

    segment_3 = LineSegment(Point(0, 0), Point(0, 5))
    self.assertEqual(
      segment_3.closest_point_to(Point(3, 3)),
      Point(0, 3)
    )
    self.assertEqual(
      segment_3.closest_point_to(Point(30, 30)),
      Point(0, 5)
    )
    self.assertEqual(
      segment_3.closest_point_to(Point(0, 2)),
      Point(0, 2)
    )


if __name__ == "__main__":
  unittest.main()
