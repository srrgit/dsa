# 110. Balanced Binary Tree (Easy)
# Given a binary tree, determine if it is height-balanced, meaning the depth of the two
# subtrees of every node never differs by more than one.
# Approach: bottom-up recursion returning -1 as a sentinel for "already unbalanced",
# otherwise the subtree height, short-circuiting further checks. Time O(n), space O(h).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node) -> int:
            if node is None:
                return 0
            left_h = height(node.left)
            if left_h == -1:
                return -1
            right_h = height(node.right)
            if right_h == -1:
                return -1
            if abs(left_h - right_h) > 1:
                return -1
            return max(left_h, right_h) + 1

        return height(root) != -1


if __name__ == "__main__":
    # [3,9,20,null,null,15,7] -> balanced
    root2 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert Solution().isBalanced(root2) == True

    # [1,2,2,3,3,null,null,4,4] -> unbalanced
    n4a, n4b = TreeNode(4), TreeNode(4)
    n3a = TreeNode(3, n4a, n4b)
    n3b = TreeNode(3)
    n2a = TreeNode(2, n3a, n3b)
    n2b = TreeNode(2)
    root1 = TreeNode(1, n2a, n2b)
    assert Solution().isBalanced(root1) == False

    assert Solution().isBalanced(None) == True
    print("All tests passed.")
