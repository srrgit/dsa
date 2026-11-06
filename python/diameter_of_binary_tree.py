# 543. Diameter of Binary Tree (Easy)
# Given the root of a binary tree, return the length (number of edges) of the
# longest path between any two nodes in the tree. The path may or may not pass
# through the root.
# Approach: post-order DFS computing the height of each subtree; at each node,
# update a global best with left_height + right_height (the longest path through
# that node), and return 1 + max(left_height, right_height) upward. Time O(n),
# Space O(h).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def height(node: Optional[TreeNode]) -> int:
            nonlocal best
            if node is None:
                return 0
            left_h = height(node.left)
            right_h = height(node.right)
            best = max(best, left_h + right_h)
            return 1 + max(left_h, right_h)

        height(root)
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
    tree1 = build_tree([1, 2, 3, 4, 5])
    assert sol.diameterOfBinaryTree(tree1) == 3

    tree2 = build_tree([1, 2])
    assert sol.diameterOfBinaryTree(tree2) == 1
    print("All tests passed.")
