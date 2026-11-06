# 98. Validate Binary Search Tree (Medium)
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# Approach: recursive range checking, passing down an allowed (low, high) open interval
# for each node's value. Time O(n), space O(h) for the recursion stack.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, low, high) -> bool:
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        return valid(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    # [2,1,3] -> valid
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    assert Solution().isValidBST(root1) == True

    # [5,1,4,null,null,3,6] -> invalid (4's subtree has 3 and 6, but 4 < 5)
    n4 = TreeNode(4, TreeNode(3), TreeNode(6))
    root2 = TreeNode(5, TreeNode(1), n4)
    assert Solution().isValidBST(root2) == False
    print("All tests passed.")
