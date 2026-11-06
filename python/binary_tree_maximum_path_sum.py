# 124. Binary Tree Maximum Path Sum (Hard)
# Given the root of a binary tree, return the maximum path sum of any path (a
# sequence of nodes connected by parent-child edges, not necessarily through the
# root, and each node used at most once).
# Approach: post-order DFS returning the best downward "gain" from each node
# (0 if negative, since we can skip that branch); at each node evaluate the path
# that goes through it (left gain + right gain + node value) against a running
# global maximum. Time O(n), Space O(h).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")

        def gain(node: Optional[TreeNode]) -> int:
            nonlocal best
            if node is None:
                return 0
            left_gain = max(gain(node.left), 0)
            right_gain = max(gain(node.right), 0)
            best = max(best, node.val + left_gain + right_gain)
            return node.val + max(left_gain, right_gain)

        gain(root)
        return best


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
    tree1 = build_tree([1, 2, 3])
    assert sol.maxPathSum(tree1) == 6

    tree2 = build_tree([-10, 9, 20, None, None, 15, 7])
    assert sol.maxPathSum(tree2) == 42
    print("All tests passed.")
