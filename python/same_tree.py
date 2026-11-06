# 100. Same Tree (Easy)
# Given the roots of two binary trees, return True if they are structurally identical and the
# corresponding nodes have the same value.
# Approach: recursive DFS comparing nodes pairwise: both None is equal, one None (not both) or
# differing values is unequal, otherwise recurse into both subtrees.
# Time: O(n), Space: O(h) recursion stack.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    sol = Solution()
    assert sol.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)),
                           TreeNode(1, TreeNode(2), TreeNode(3))) is True
    assert sol.isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))) is False
    assert sol.isSameTree(TreeNode(1, TreeNode(2), TreeNode(1)),
                           TreeNode(1, TreeNode(1), TreeNode(2))) is False
    print("All tests passed.")
