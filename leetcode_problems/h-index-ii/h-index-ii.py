# https://leetcode.com/problems/h-index-ii/
from typing import List
from math import ceil, floor
import unittest


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # h of N papers have at least h citations each,
        # and the other N − h papers have no more than h citations each
        # h is between 0 and len(citations)
        if len(citations) == 0:
            return 0

        if len(citations) == 1 and citations[0] > 0:
            return 1

        idx = len(citations)

        if citations[0] >= idx:
            return idx

        idx -= 1

        while idx >= 0:
            if citations[-idx] >= idx and citations[-idx-1] <= idx:
                return idx
            idx -= 1
        return 0

class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case_1(self):
        citations = [0, 1, 3, 5, 6]
        self.assertEqual(self.solution.hIndex(citations), 3)

    def test_example_case_2(self):
        citations = [11,15]
        self.assertEqual(self.solution.hIndex(citations), 2)

    def test_wikipedia_case_1(self):
        citations = [3, 4, 5, 8, 10]
        self.assertEqual(self.solution.hIndex(citations), 4)

    def test_wikipedia_case_2(self):
        citations = [3, 3, 5, 8, 25]
        self.assertEqual(self.solution.hIndex(citations), 3)

    def test_gotcha(self):
        citations = [1]
        self.assertEqual(self.solution.hIndex(citations), 1)

    def test_gotcha_ii(self):
        citations = [100]
        self.assertEqual(self.solution.hIndex(citations), 1)

    def test_gotcha_iii(self):
        citations = [0]
        self.assertEqual(self.solution.hIndex(citations), 0)

    def test_gotcha_iii(self):
        citations = []
        self.assertEqual(self.solution.hIndex(citations), 0)


if __name__ == '__main__':
    unittest.main()
