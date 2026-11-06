# 102. Binary Tree Level Order Traversal (Medium)
# Given the root of a binary tree, return the values of its nodes as a list
# of lists, where each inner list contains the values of one level,
# traversed left to right, top to bottom.
#
# Approach: standard BFS using a queue, processing one full level at a time
# by snapshotting the current queue length before enqueuing children.
# Time: O(n), Space: O(n).

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result


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
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    assert sol.levelOrder(root1) == [[3], [9, 20], [15, 7]]

    root2 = build_tree([1])
    assert sol.levelOrder(root2) == [[1]]

    assert sol.levelOrder(None) == []

    print("All test cases passed for 102. Binary Tree Level Order Traversal")
