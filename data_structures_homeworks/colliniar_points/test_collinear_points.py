import unittest
from point import Point
from line_segment import LineSegment
from collinear_points import CollinearPoints, SlopeAndPoint


class TestPoint(unittest.TestCase):
    def test_init(self):
        point = Point(1, 3)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 3)

    def test_slope_to(self):
        point = Point(0, 0)
        self.assertEqual(point.slope_to(Point(1, 0)), 0)
        self.assertEqual(point.slope_to(Point(1, 2)), 2)
        self.assertEqual(point.slope_to(Point(2, -4)), -2)
        self.assertEqual(point.slope_to(Point(-4, 2)), -0.5)
        self.assertEqual(point.slope_to(Point(0, 1)), float('inf'))
        self.assertEqual(point.slope_to(Point(0, -1)), float('-inf'))

    def test_compare_to(self):
        point = Point(0, 0)
        self.assertEqual(point.compare_to(Point(1, 0)), -1)
        self.assertEqual(point.compare_to(Point(0, 1)), -1)
        self.assertEqual(point.compare_to(Point(-1, -4)), 1)
        self.assertEqual(point.compare_to(Point(-1, -2)), 1)
        self.assertEqual(point.compare_to(Point(0, 0)), 0)


class TestCollinearPoints(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.point_1 = Point(0, 0)
        cls.point_2 = Point(3, 4)
        cls.point_3 = Point(4, 9)
        cls.point_4 = Point(5, 8)
        cls.point_5 = Point(6, 7)

        cls.points = [
            cls.point_1,
            cls.point_2,
            cls.point_3,
            cls.point_4,
            cls.point_5
        ]

        cls.collinear_points = CollinearPoints(cls.points)

    def test_get_slopes_and_points(self):
        actual = self.collinear_points.get_slopes_and_points(
            self.point_1)
        expected = [
            SlopeAndPoint(slope=self.point_1.slope_to(self.point_1), point=self.point_1), 
            SlopeAndPoint(slope=self.point_1.slope_to(self.point_2), point=self.point_2),
            SlopeAndPoint(slope=self.point_1.slope_to(self.point_3), point=self.point_3),
            SlopeAndPoint(slope=self.point_1.slope_to(self.point_4), point=self.point_4),
            SlopeAndPoint(slope=self.point_1.slope_to(self.point_5), point=self.point_5)
        ]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
