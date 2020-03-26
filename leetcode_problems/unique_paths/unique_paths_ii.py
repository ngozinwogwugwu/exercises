
import unittest
import numpy as np

class Solution(object):
    def uniquePathsWithObstacles(self, obstacle_grid):
        """
        :type obstacle_grid: List[List[int]]
        :rtype: int
        """
        m = len(obstacle_grid)
        n = len(obstacle_grid[0])

        self.grid = np.zeros((m, n), dtype=int)

        if obstacle_grid[m - 1][n - 1] is 0:
            self.grid[m - 1][n - 1] = 1

        current_m = m - 1
        current_n = n - 1

        while current_n >= 0:
            while current_m > 0:
                current_m -= 1
                if obstacle_grid[current_m][current_n] is 0:
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

    def test_uniquePathsWithObstacles_simple(self):
        input = [
          [0,0,0],
          [0,1,0],
          [0,0,0]
        ]
        expected = 2
        self.assertEqual(expected, self.solution.uniquePathsWithObstacles(input))

    def test_uniquePathsWithObstacles_gotcha(self):
        input = [[1]]
        expected = 0
        self.assertEqual(expected, self.solution.uniquePathsWithObstacles(input))


if __name__ == '__main__':
    unittest.main()
