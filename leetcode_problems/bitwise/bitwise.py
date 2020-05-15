# https://leetcode.com/problems/bitwise-and-of-numbers-range/submissions/
from typing import List
import unittest
from math import log, ceil


class Solution:
    def rangeBitwiseAnd(self, lo, hi):
        len_range = hi - lo + 1
        if len_range == 0:
            return lo

        max_int = 2147483647
        num_shifts = ceil(log((len_range), 2))
        adder = max_int * (2**num_shifts)
        return hi & lo & adder

    def brute_force(self, lo: int, hi: int) -> int:
        adder = lo
        for i in range(lo, hi + 1):
            adder = adder & i

        return adder


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(1, 2), 0)
        self.assertEqual(self.solution.rangeBitwiseAnd(5, 7), 4)
        self.assertEqual(self.solution.rangeBitwiseAnd(0, 1), 0)
        self.assertEqual(self.solution.rangeBitwiseAnd(0, 2147483647), 0)
        self.assertEqual(self.solution.rangeBitwiseAnd(
            600000000, 2147483647), 0)

    def test_more(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(0, 0), 0)
        self.assertEqual(self.solution.rangeBitwiseAnd(3, 6), 0)
        self.assertEqual(self.solution.rangeBitwiseAnd(6, 12), 0)

    def test_brute_force(self):
        self.assertEqual(self.solution.brute_force(1, 2), 0)
        self.assertEqual(self.solution.brute_force(5, 7), 4)
        self.assertEqual(self.solution.brute_force(0, 1), 0)


if __name__ == '__main__':
    unittest.main()
