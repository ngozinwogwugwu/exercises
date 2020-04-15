import unittest

class Solution(object):
    def PredictTheWinner(self, nums):
        ## if all numbers are the same, or there are even numbers, or if there are fewer than three entries
        if len(set(nums)) == 1 or len(nums) < 3 or len(nums)%2 == 0:
            return True

        if nums[int(len(nums)/2)] >= sum(nums)/2:
            return False

        head = nums[0]
        next_head = nums[1]

        tail = nums[-1]
        next_tail = nums[-2]

        if head > max(tail, next_head) or tail > max(head, next_tail):
            return True

        return False




class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_predict_base(self):
        self.assertFalse(self.solution.PredictTheWinner([1, 5, 2]))
        self.assertTrue(self.solution.PredictTheWinner([1, 5, 233, 7]))

    def test_predict_gotcha(self):
        self.assertTrue(self.solution.PredictTheWinner([1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(self.solution.PredictTheWinner([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))

    def test_predict_real(self):
        self.assertFalse(self.solution.PredictTheWinner([2,4,55,6,8]))

    def [1000,1000,1000,0,0,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]



if __name__ == '__main__':
    unittest.main()
