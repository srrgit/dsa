# 236. Lowest Common Ancestor of a Binary Tree (Medium)
# Given the root of a binary tree and two nodes p and q in the tree, return their
# lowest common ancestor (the deepest node that has both p and q as descendants,
# where a node can be a descendant of itself).
# Approach: recursive DFS — if the current node is None or equals p or q, return
# it; otherwise recurse into both children. If both sides return a non-null
# result, the current node is the LCA; otherwise propagate whichever side is
# non-null. Time O(n), Space O(h).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right


def build_tree_with_index(values):
    """Build tree and return (root, {val: node}) for easy lookup in tests."""
    if not values or values[0] is None:
        return None, {}
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = iter(nodes[1:])
    for node in nodes:
        if node:
            node.left = next(kids, None)
            node.right = next(kids, None)
    index = {node.val: node for node in nodes if node}
    return nodes[0], index


if __name__ == "__main__":
    sol = Solution()
    root, idx = build_tree_with_index([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert sol.lowestCommonAncestor(root, idx[5], idx[1]) is idx[3]
    assert sol.lowestCommonAncestor(root, idx[5], idx[4]) is idx[5]
    assert sol.lowestCommonAncestor(root, idx[6], idx[4]) is idx[5]
    print("All tests passed.")
