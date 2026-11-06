# 108. Convert Sorted Array to Binary Search Tree (Easy)
# Given an integer array sorted in ascending order, convert it to a
# height-balanced binary search tree.
#
# Approach: recursive divide and conquer. Pick the middle element of the
# current subarray as the root (biasing toward the lower middle on ties)
# so the tree stays height-balanced, then recursively build the left and
# right subtrees from the left and right subarrays. Time: O(n),
# Space: O(log n) recursion stack (O(n) for the output tree).

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(nums[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(nums) - 1)


def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def is_height_balanced(node):
    def height(n):
        if not n:
            return 0
        lh = height(n.left)
        if lh == -1:
            return -1
        rh = height(n.right)
        if rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)

    return height(node) != -1


if __name__ == "__main__":
    sol = Solution()

    tree1 = sol.sortedArrayToBST([-10, -3, 0, 5, 9])
    assert inorder(tree1) == [-10, -3, 0, 5, 9]
    assert is_height_balanced(tree1) is True

    tree2 = sol.sortedArrayToBST([1, 3])
    assert inorder(tree2) == [1, 3]
    assert is_height_balanced(tree2) is True

    assert sol.sortedArrayToBST([]) is None

    print("All test cases passed for 108. Convert Sorted Array to Binary Search Tree")
