# 104. Maximum Depth of Binary Tree (Easy)
# Given the root of a binary tree, return its maximum depth: the number of nodes along the
# longest path from the root down to the farthest leaf node.
# Approach: recursive DFS, depth = 1 + max(depth(left subtree), depth(right subtree)).
# Time: O(n), Space: O(h) recursion stack.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.maxDepth(root) == 3
    assert sol.maxDepth(None) == 0
    assert sol.maxDepth(TreeNode(1)) == 1
    print("All tests passed.")
