# 101. Symmetric Tree (Easy)
# Given the root of a binary tree, check whether it is a mirror of itself (i.e.
# symmetric around its center).
# Approach: recursively compare the left and right subtrees as mirror images —
# two trees are mirrors if their root values match and each one's left mirrors
# the other's right (and vice versa). Time O(n), Space O(h).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return (
                t1.val == t2.val
                and is_mirror(t1.left, t2.right)
                and is_mirror(t1.right, t2.left)
            )

        return is_mirror(root, root)


def build_tree(values):
    if not values or values[0] is None:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = iter(nodes[1:])
    for node in nodes:
        if node:
            node.left = next(kids, None)
            node.right = next(kids, None)
    return nodes[0]


if __name__ == "__main__":
    sol = Solution()
    tree1 = build_tree([1, 2, 2, 3, 4, 4, 3])
    assert sol.isSymmetric(tree1) is True

    tree2 = build_tree([1, 2, 2, None, 3, None, 3])
    assert sol.isSymmetric(tree2) is False
    print("All tests passed.")
