# https://leetcode.com/problems/delete-leaves-with-a-given-value/
from typing import List
import unittest

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.val)
        return str([self.val, self.left, self.right])


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root.left is not None:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right is not None:
            root.right = self.removeLeafNodes(root.right, target)

        if root.left is None and root.right is None and root.val == target:
            return None
        return root


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case_1(self):
        left = TreeNode(2, left=TreeNode(2))
        right = TreeNode(3, left=TreeNode(2), right=TreeNode(4))
        root = TreeNode(1, left=left, right=right)

        print(root)
        print(self.solution.removeLeafNodes(root, 2))

    def test_example_case_2(self):
        left = TreeNode(3, left=TreeNode(3), right=TreeNode(2))
        root = TreeNode(1, left=left, right=TreeNode(3))

        print(root)
        print(self.solution.removeLeafNodes(root, 3))


    def test_example_case_3(self):
        root = TreeNode(
            val=1,
            left=TreeNode(
                val=2,
                left=TreeNode(
                    val=2,
                    left=TreeNode(val=2)
                )
            )
        )

        print(root)
        print(self.solution.removeLeafNodes(root, 2))


if __name__ == '__main__':
    unittest.main()
