# [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

``` python
from functools import reduce
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        zigzag_vals = [[root.val]]
        parent_nodes = [root]

        while True:
            child_nodes = []
            child_vals = []
            # todo - figure out the functional way to do this
            for parent_node in parent_nodes: 
                if parent_node.left is not None:
                    child_nodes.append(parent_node.left)
                    child_vals.append(parent_node.left.val)

                if parent_node.right is not None:
                    child_nodes.append(parent_node.right)
                    child_vals.append(parent_node.right.val)

            # filter out none values
            if len(child_nodes) < 1:
                break

            zigzag_vals.append(child_vals)
            parent_nodes = child_nodes

        # let's zig zag these vals
        for tree_layer_index in range(zig_zag_vals):
            if (tree_layer_index % 2) == 1:
                zig_zag_vals[tree_layer_index].reverse()


        return [parent_vals, child_vals.reverse(), grandchild_vals]```
