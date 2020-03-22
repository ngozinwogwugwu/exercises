import unittest
import numpy as np

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.grid = np.zeros((m, n), dtype=int)
        self.grid[m - 1][n - 1] = 1

        current_m = m - 1
        current_n = n - 1

        while current_n >= 0:
            while current_m > 0:
                current_m -= 1
                right_neighbor = self.get_grid_value(current_m, current_n + 1)
                down_neighbor = self.get_grid_value(current_m + 1, current_n)
                self.grid[current_m][current_n] = right_neighbor + down_neighbor

            current_m = m
            current_n -= 1

        return self.grid[0][0]


    def get_grid_value(self, n, m):
        try:
            return self.grid[n][m]
        except Exception as e:
            return 0

class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_uniquePaths_simple(self):
        n = 4
        m = 3
        expected = 10
        self.assertEqual(expected, self.solution.uniquePaths(m, n))

    def test_uniquePaths_standard(self):
        n = 7
        m = 3
        expected = 28
        self.assertEqual(expected, self.solution.uniquePaths(m, n))

    def test_uniquePaths_standard(self):
        n = 23
        m = 12
        expected = 193536720
        self.assertEqual(expected, self.solution.uniquePaths(m, n))


if __name__ == '__main__':
    unittest.main()
