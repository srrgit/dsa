# 199. Binary Tree Right Side View (Medium)
# Given the root of a binary tree, return the values of the nodes visible
# when the tree is viewed from the right side, ordered top to bottom.
#
# Approach: BFS level-order traversal; for each level, the last node
# processed is the rightmost one visible from the right side.
# Time: O(n), Space: O(n) for the queue in the worst case.

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result


def build_tree(values):
    # values use None for missing nodes, in level order (LeetCode style)
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

    root1 = build_tree([1, 2, 3, None, 5, None, 4])
    assert sol.rightSideView(root1) == [1, 3, 4]

    root2 = build_tree([1, None, 3])
    assert sol.rightSideView(root2) == [1, 3]

    assert sol.rightSideView(None) == []

    print("All test cases passed for 199. Binary Tree Right Side View")
