# https://leetcode.com/problems/palindrome-number/
from typing import List
import unittest

class Solution:
    def isStrPalindrome(self, str_x: int) -> bool:
      for i in range(len(str_x)):
        if str_x[i] != str_x[-1-i]:
          return False
      return True

    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return self.isStrPalindrome(str_x)


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case_1(self):
        self.assertEqual(self.solution.isPalindrome(121), True)

    def test_example_case_2(self):
        self.assertEqual(self.solution.isPalindrome(-121), False)


if __name__ == '__main__':
    unittest.main()
