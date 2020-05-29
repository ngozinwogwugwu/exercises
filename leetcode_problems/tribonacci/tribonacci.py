# https://leetcode.com/problems/n-th-tribonacci-number/
from typing import List
import unittest

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        i = 2
        t_i_3 = 0
        t_i_2 = 1
        t_i_1 = 1
        t = 0

        while i < n:
            i += 1
            t = t_i_1 + t_i_2 + t_i_3
            t_i_3 = t_i_2
            t_i_2 = t_i_1
            t_i_1 = t

        return t



class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case_1(self):
        self.assertEqual(self.solution.tribonacci(4), 4)

    def test_example_case_2(self):
        self.assertEqual(self.solution.tribonacci(25), 1389537)


if __name__ == '__main__':
    unittest.main()
