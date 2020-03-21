import unittest


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.move(n - 1, m - 1)

    def move(self, right_moves_remaining, down_moves_remaining):
        if right_moves_remaining < 0 and down_moves_remaining < 0:
            return 0

        if right_moves_remaining == 0 and down_moves_remaining == 0:
            return 1

        moves_available = 0
        if right_moves_remaining > 0:
            moves_available += self.move(right_moves_remaining - 1,
                                         down_moves_remaining)
        if down_moves_remaining > 0:
            moves_available += self.move(right_moves_remaining,
                                         down_moves_remaining - 1)

        return moves_available


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_uniquePaths_simple(self):
        n = 3
        m = 2
        expected = 3
        self.assertEqual(expected, self.solution.uniquePaths(m, n))

    def test_uniquePaths_standard(self):
        n = 7
        m = 3
        expected = 28
        self.assertEqual(expected, self.solution.uniquePaths(m, n))

    # def test_uniquePaths_standard(self):
    #     n = 23
    #     m = 12
    #     expected = 28
    #     self.assertEqual(expected, self.solution.uniquePaths(m, n))


if __name__ == '__main__':
    unittest.main()
