# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
from typing import List
import unittest


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_run = 0
        if len(nums) == 0:
            return max_run
        current_run = 0
        previous_number = float("-inf")

        for current_number in nums:
            if current_number > previous_number:
                current_run += 1
            else:
                current_run = 1

            if current_run > max_run:
                max_run = current_run

            previous_number = current_number

        return max_run


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case(self):
        example_array = [1, 3, 5, 4, 7]
        self.assertEqual(self.solution.findLengthOfLCIS(example_array), 3)

    def test_example_case_2(self):
        example_array = [2, 2, 2, 2, 2]
        self.assertEqual(self.solution.findLengthOfLCIS(example_array), 1)

    def test_example_case_3(self):
        example_array = [1, 3, 5, 4, 2, 3, 4, 5]
        self.assertEqual(self.solution.findLengthOfLCIS(example_array), 4)


if __name__ == '__main__':
    unittest.main()
