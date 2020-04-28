# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3297/
from typing import List
import unittest

class Solution(object):
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]

        stones.sort()
        [big_stone, bigger_stone] = stones[-2:]
        stones = stones[:-2]

        remains = bigger_stone - big_stone
        if remains != 0:
            stones.append(remains)

        return self.lastStoneWeight(stones)


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case(self):
        stones = [2,7,4,1,8,1]
        self.assertEqual(self.solution.lastStoneWeight(stones), 1)

if __name__ == '__main__':
    unittest.main()
