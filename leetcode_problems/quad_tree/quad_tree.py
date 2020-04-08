import unittest
from math import floor

# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        allVals = self.allValsInGrid(grid)
        isLeaf = len(allVals) is 1

        if isLeaf:
            return Node(allVals[0], isLeaf, None, None, None, None)

        else:
            boundary = int(floor(len(grid)/2))
            return Node(
                val=1,
                isLeaf=isLeaf,
                topLeft = self.construct([row[:boundary] for row in grid[:boundary]]),
                topRight = self.construct([row[boundary:] for row in grid[:boundary]]),
                bottomLeft = self.construct([row[:boundary] for row in grid[boundary:]]),
                bottomRight = self.construct([row[boundary:] for row in grid[boundary:]]),
            )

    def allValsInGrid(self, grid):
        allValsInGrid = []
        for row in grid:
            allValsInGrid += row
        return list(set(allValsInGrid))

# class TestSolution(unittest.TestCase):
#     solution = Solution()

#     def test_quadTree_example_1(self):
#         grid = [
#             [0,1],
#             [1,0]
#         ]
#         expected = [
#             [0,1],
#             [1,0],[1,1],[1,1],[1,0]
#         ]

#         actual = self.solution.construct(grid)
#         import pdb; pdb.set_trace()
#         self.assertEqual(actual, expected)

#     def test_quadTree_example_2(self):
#         grid = [
#             [1,1,1,1,0,0,0,0],
#             [1,1,1,1,0,0,0,0],
#             [1,1,1,1,1,1,1,1],
#             [1,1,1,1,1,1,1,1],
#             [1,1,1,1,0,0,0,0],
#             [1,1,1,1,0,0,0,0],
#             [1,1,1,1,0,0,0,0],
#             [1,1,1,1,0,0,0,0]
#         ]
#         expected = [
#             [0,1],
#             [1,1], [0,1], [1,1], [1,0],
#             None, None, None, None,
#             [1,0],[1,0],[1,1],[1,1]
#         ]

#     def test_quadTree_example_3(self):
#         grid = [
#             [1,1],
#             [1,1]
#         ]
#         expected = [[1,1]]

#     def test_quadTree_example_4(self):
#         grid = [[0]]
#         expected = [[1,0]]


#     def test_quadTree_example_5(self):
#         grid = [
#             [1,1,0,0],
#             [1,1,0,0],
#             [0,0,1,1],
#             [0,0,1,1]
#         ]
#         expected = [
#             [0,1],
#             [1,1],[1,0],[1,0],[1,1]
#         ]

if __name__ == '__main__':
    unittest.main()
