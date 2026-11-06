# 230. Kth Smallest Element in a BST (Medium)
# Given the root of a binary search tree and an integer k, return the kth smallest value
# (1-indexed) among all values in the tree.
# Approach: an in-order traversal of a BST visits nodes in ascending order; use an iterative,
# stack-based in-order traversal and stop as soon as the kth visited node is reached.
# Time: O(h + k), Space: O(h).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        count = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            node = node.right
        return -1


if __name__ == "__main__":
    sol = Solution()
    root1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    assert sol.kthSmallest(root1, 1) == 1

    root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    assert sol.kthSmallest(root2, 3) == 3
    assert sol.kthSmallest(root1, 4) == 4
    print("All tests passed.")
