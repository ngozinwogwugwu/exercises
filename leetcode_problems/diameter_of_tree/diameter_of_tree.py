# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3293/
from typing import List
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        left_depths = self.get_depths(root.left) if root is not None else []
        right_depths = self.get_depths(root.right) if root is not None else []
        left_depths.sort()
        right_depths.sort()

        left_max, right_max, left_second_max, right_second_max = 0, 0, 0, 0

        if len(left_depths) > 0:
            left_max = left_depths[-1]
        if len(left_depths) > 1:
            left_second_max = left_depths[-2]
        if len(right_depths) > 0:
            right_max = right_depths[-1]
        if len(right_depths) > 1:
            right_second_max = right_depths[-2]

        tentative_diameter = left_max + right_max
        if (left_max + left_second_max - 2) > left_max + right_max:
            left_diameter = self.diameterOfBinaryTree(root.left)
            return left_diameter if left_diameter > tentative_diameter else tentative_diameter
        if (right_max + right_second_max - 2) > left_max + right_max:
            right_diameter = self.diameterOfBinaryTree(root.right)
            return right_diameter if right_diameter > tentative_diameter else tentative_diameter
        return tentative_diameter

    def get_depths(self, node: TreeNode, current_depth: int = 1) -> List[int]:
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [current_depth]

        return self.get_depths(node.left, current_depth + 1) + self.get_depths(node.right, current_depth + 1)


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case(self):
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
        left = TreeNode(2, TreeNode(4), TreeNode(5))
        right = TreeNode(3)
        root = TreeNode(1, left, right)

        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)


    def test_my_case(self):
        #           1
        #          / \
        #         2   3
        #        / \
        #       4   5
        #      / \   \
        #     6   7   8
        #          \   \
        #           9   10
        ten = TreeNode(10)
        nine = TreeNode(9)
        eight = TreeNode(8, None, ten)
        seven = TreeNode(7, None, nine)
        six = TreeNode(6)
        five = TreeNode(5, None, eight)
        four = TreeNode(4, six, seven)
        three = TreeNode(3)
        two = TreeNode(2, four, five)
        root = TreeNode(1, two, three)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 6)

    def test_gotcha(self):
        #             1
        #            /
        #           5
        #          /
        #         3
        #        / \
        #       1   4
        one = TreeNode(1)
        four = TreeNode(4)
        three = TreeNode(3, one, four)
        five = TreeNode(5, three)
        root = TreeNode(1, five)

        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)


if __name__ == '__main__':
    unittest.main()
