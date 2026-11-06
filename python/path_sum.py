# 112. Path Sum (Easy)
# Given the root of a binary tree and an integer targetSum, return true if
# the tree has a root-to-leaf path such that the sum of the values along
# the path equals targetSum.
#
# Approach: DFS, subtracting the current node's value from the remaining
# target as we descend. At a leaf, check whether the remaining target has
# been reduced to exactly 0. Time: O(n), Space: O(h) recursion stack
# (h = tree height).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        remaining = targetSum - root.val
        if not root.left and not root.right:
            return remaining == 0
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)


def build_tree(values):
    if not values or values[0] is None:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


if __name__ == "__main__":
    sol = Solution()
    root1 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    assert sol.hasPathSum(root1, 22) is True

    root2 = build_tree([1, 2, 3])
    assert sol.hasPathSum(root2, 5) is False

    assert sol.hasPathSum(None, 0) is False

    print("All test cases passed for 112. Path Sum")
