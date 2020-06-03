# https://leetcode.com/problems/valid-parentheses/
import unittest

class Solution:
  def isValid(self, s: str) -> bool:
    open_bracks = []
    bracket_dict = {
      ')': '(',
      '}': '{',
      ']': '['
    }

    for char in s:
      if char in bracket_dict.values(): # open bracket
        open_bracks.append(char)
      elif char in bracket_dict.keys(): # close bracket
        if len(open_bracks) == 0:
          return False

        if bracket_dict[char] is not open_bracks.pop():
          return False
      else:
        raise Exception

    return len(open_bracks) == 0

class TestSolution(unittest.TestCase):
  solution = Solution()

  def test_example_case_1(self):
    self.assertEqual(self.solution.isValid(""), True)

  def test_example_case_2(self):
    self.assertEqual(self.solution.isValid("()"), True)

  def test_example_case_3(self):
    self.assertEqual(self.solution.isValid("()[]{}"), True)

  def test_example_case_4(self):
    self.assertEqual(self.solution.isValid("(]"), False)

  def test_example_case_5(self):
    self.assertEqual(self.solution.isValid("([)]"), False)

  def test_example_case_6(self):
    self.assertEqual(self.solution.isValid("{[]}"), True)

  def test_example_case_7(self):
    self.assertEqual(self.solution.isValid("]"), False)


if __name__ == '__main__':
  unittest.main()
