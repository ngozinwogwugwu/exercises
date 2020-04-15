import unittest

class Solution(object):
    def isMatch(self, string, pattern):
        s_idx = len(string) - 1
        p_idx = len(pattern) - 1

        while p_idx >= 0:
            if pattern[p_idx] is "*":
                p_idx -= 1

                if pattern[p_idx] is '.':
                    return True

                while string[s_idx] is pattern[p_idx] and s_idx >= 0:
                    s_idx -= 1
                p_idx -= 1

            elif  pattern[p_idx] is "." or pattern[p_idx] is string[s_idx]:
                s_idx -= 1
                p_idx -= 1

            else:
                return False

        return s_idx is p_idx
        
class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_0(self):
        self.assertFalse(self.solution.isMatch("aa", "a"))
        self.assertTrue(self.solution.isMatch("aa", "aa"))
        self.assertTrue(self.solution.isMatch("trouble", "trouble"))
        self.assertFalse(self.solution.isMatch("trouble", "tree"))
        self.assertFalse(self.solution.isMatch("tree", "trouble"))

    def test_1(self):
        self.assertFalse(self.solution.isMatch("aa", "."))
        self.assertTrue(self.solution.isMatch("aa", "a."))
        self.assertTrue(self.solution.isMatch("trouble", "tr.uble"))
        self.assertFalse(self.solution.isMatch("trouble", "tr.e"))
        self.assertFalse(self.solution.isMatch("tree", "trou.le"))

    def test_2(self):
        self.assertTrue(self.solution.isMatch("aa", "a*"))
        self.assertTrue(self.solution.isMatch("baaaab", "ba*b"))
        self.assertFalse(self.solution.isMatch("caaab", "ba*b"))

    def test_3(self):
        self.assertTrue(self.solution.isMatch("ab", ".*"))

    def test_4(self):
        self.assertTrue(self.solution.isMatch("cccb", "c*a*b"))
        self.assertFalse(self.solution.isMatch("ccb", "c*a*c"))
        self.assertTrue(self.solution.isMatch("aab", "c*a*b"))
        self.assertFalse(self.solution.isMatch("daab", "c*a*b"))
        self.assertTrue(self.solution.isMatch("cab", "c*a*b"))
        self.assertTrue(self.solution.isMatch("ccaab", "c*a*b"))

    def test_5(self):
        self.assertTrue(self.solution.isMatch("mississippi", "mis*is*ip*."))
        self.assertFalse(self.solution.isMatch("mississippi", "mis*is*p*."))

if __name__ == '__main__':
    unittest.main()
