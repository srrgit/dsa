# 863. All Nodes Distance K in Binary Tree (Medium)
# Given the root of a binary tree, a `target` node's value, and an integer
# `k`, return the values of all nodes that are exactly distance k from the
# target node (distance measured in the undirected version of the tree).
#
# Approach: first DFS to build a map from each node to its parent, which lets
# us treat the tree as an undirected graph. Then BFS outward from the target
# node (via left, right, and parent pointers) for exactly k steps. O(n) time,
# O(n) space.

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def record_parents(node, par):
            if not node:
                return
            parent[node] = par
            record_parents(node.left, node)
            record_parents(node.right, node)

        record_parents(root, None)

        visited = {target}
        queue = deque([target])
        dist = 0
        while queue and dist < k:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in (node.left, node.right, parent[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            dist += 1

        return [node.val for node in queue]


def build_sample_tree():
    #         3
    #        / \
    #       5   1
    #      / \ / \
    #     6  2 0  8
    #       / \
    #      7   4
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n0 = TreeNode(0)
    n8 = TreeNode(8)
    n7 = TreeNode(7)
    n4 = TreeNode(4)
    n3.left, n3.right = n5, n1
    n5.left, n5.right = n6, n2
    n1.left, n1.right = n0, n8
    n2.left, n2.right = n7, n4
    return n3, n5


if __name__ == "__main__":
    sol = Solution()
    root, target = build_sample_tree()
    assert sorted(sol.distanceK(root, target, 2)) == [1, 4, 7]
    assert sorted(sol.distanceK(root, target, 0)) == [5]
    assert sorted(sol.distanceK(root, root, 1)) == [1, 5]
    print("All tests passed.")
