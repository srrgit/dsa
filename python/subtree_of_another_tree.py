# 572. Subtree of Another Tree (Easy)
# Given the roots of two binary trees root and subRoot, return true if
# there is a subtree of root with the same structure and node values as
# subRoot.
#
# Approach: for every node in root, check whether the tree rooted there is
# structurally identical to subRoot (a standard "same tree" comparison).
# Time: O(m * n) worst case (m, n = sizes of the two trees),
# Space: O(max(height(root), height(subRoot))) recursion stack.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self._same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def _same_tree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return self._same_tree(a.left, b.left) and self._same_tree(a.right, b.right)


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
    root1 = build_tree([3, 4, 5, 1, 2])
    sub1 = build_tree([4, 1, 2])
    assert sol.isSubtree(root1, sub1) is True

    root2 = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    sub2 = build_tree([4, 1, 2])
    assert sol.isSubtree(root2, sub2) is False

    print("All test cases passed for 572. Subtree of Another Tree")
