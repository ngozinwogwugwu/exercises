import unittest
from point import Point
from line_segment import LineSegment
from collinear_points import CollinearPoints


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
        self.assertEqual(point.__lt__(Point(1, 0)), True)
        self.assertEqual(point.__lt__(Point(0, 1)), True)
        self.assertEqual(point.__lt__(Point(-1, -4)), False)
        self.assertEqual(point.__lt__(Point(-1, -2)), False)
        self.assertEqual(point.__lt__(Point(0, 0)), False)


class TestCollinearPoints(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.point_1 = Point(0, 0)
        cls.point_2 = Point(3, 4)
        cls.point_3 = Point(4, 9)
        cls.point_4 = Point(5, 8)
        cls.point_5 = Point(6, 7)
        cls.point_6 = Point(6, 8)
        cls.point_7 = Point(9, 12)
        cls.point_8 = Point(12, 16)

        cls.points = [
            cls.point_1,
            cls.point_2,
            cls.point_3,
            cls.point_4,
            cls.point_5,
            cls.point_6,
            cls.point_7,
            cls.point_8
        ]

        cls.collinear_points = CollinearPoints(cls.points)

    def test_get_slopes_and_points(self):
        actual = self.collinear_points.get_sets_of_qualifying_points(
            self.point_1)
        expected = [[self.point_2, self.point_6, self.point_7, self.point_8]]

        self.assertEqual(actual, expected)

    def test_get_collinear_line_segments_for_single_point(self):
        line_segment = self.collinear_points.get_collinear_line_segments_for_single_point(
            self.point_1)[0]
        self.assertEqual(line_segment.p, self.point_1)
        self.assertEqual(line_segment.q, self.point_8)




if __name__ == "__main__":
    unittest.main()
