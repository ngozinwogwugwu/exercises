# https://leetcode.com/problems/reverse-integer/
from typing import List
import unittest

class Solution:
    def reverse(self, x: int) -> int:
        negative_multiplier = 1

        if x < 0:
            negative_multiplier = -1
            x = -x
        
        digits = []
        
        while x > 0:
            ones_place = x % 10
            digits.append(int(ones_place))
            x = (x - ones_place)/10
        
        digits.reverse()
        multiplier = 1
        output = 0
        
        for digit in digits:
            output += digit*multiplier
            multiplier *= 10

        return negative_multiplier * output

class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.reverse(123), 321)
        self.assertEqual(self.solution.reverse(-123), -321)
        self.assertEqual(self.solution.reverse(120), 21)


if __name__ == '__main__':
    unittest.main()
