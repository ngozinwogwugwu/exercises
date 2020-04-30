# https://leetcode.com/problems/string-matching-in-an-array/
from typing import List
import unittest

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len)
        substrings = []

        for idx, word in enumerate(words):
            for bigger_word in words[idx+1:]:
                if word in bigger_word:
                    substrings.append(word)
                    break

        return substrings


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case_1(self):
        given_input = ["mass","as","hero","superhero"]
        expected_output = ["as","hero"]
        self.assertEqual(self.solution.stringMatching(given_input), expected_output)

    def test_example_case_2(self):
        given_input = ["leetcode","et","code"]
        expected_output = ["et","code"]
        self.assertEqual(self.solution.stringMatching(given_input), expected_output)

    def test_example_case_3(self):
        given_input = ["blue","green","bu"]
        expected_output = []
        self.assertEqual(self.solution.stringMatching(given_input), expected_output)


if __name__ == '__main__':
    unittest.main()
