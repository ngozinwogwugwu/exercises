# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from typing import List
import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        letter_positions = {}
        back_idx = 0
        front_idx = 0
        max_length = 0

        while front_idx < len(s):
            current_letter = s[front_idx]

            if current_letter in letter_positions and letter_positions[current_letter] >= back_idx:
                back_idx = letter_positions[current_letter] + 1

            letter_positions[current_letter] = front_idx
            current_length = front_idx - back_idx + 1
            if current_length > max_length:
                max_length = current_length
            front_idx += 1

        return max_length


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_cases(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)


if __name__ == '__main__':
    unittest.main()
