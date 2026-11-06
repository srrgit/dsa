# 226. Invert Binary Tree (Easy)
# Given the root of a binary tree, invert the tree (swap every left and right
# child) and return its root.
# Approach: recursively swap the left and right subtrees of every node.
# Time O(n), Space O(h) for the recursion stack.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


def build_tree(values):
    """Build a tree from a level-order list with None for missing nodes."""
    if not values or values[0] is None:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = iter(nodes[1:])
    for node in nodes:
        if node:
            node.left = next(kids, None)
            node.right = next(kids, None)
    return nodes[0]


def level_order(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    sol = Solution()
    tree = build_tree([4, 2, 7, 1, 3, 6, 9])
    inverted = sol.invertTree(tree)
    assert level_order(inverted) == [4, 7, 2, 9, 6, 3, 1]

    tree2 = build_tree([2, 1, 3])
    inverted2 = sol.invertTree(tree2)
    assert level_order(inverted2) == [2, 3, 1]

    assert sol.invertTree(None) is None
    print("All tests passed.")
