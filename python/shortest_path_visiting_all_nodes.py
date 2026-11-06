# 847. Shortest Path Visiting All Nodes (Hard)
# Given an undirected connected graph as an adjacency list `graph`, return the
# length of the shortest path that visits every node at least once, starting
# and ending anywhere, revisiting nodes/edges allowed.
#
# Approach: BFS over states (current_node, visited_mask). Start from every node
# simultaneously with its own singleton mask; the first time a state reaches
# the full mask (all bits set) gives the shortest path length. O(2^n * n^2)
# time/space in the worst case.

from typing import List
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        full_mask = (1 << n) - 1

        queue = deque()
        visited = set()
        for i in range(n):
            state = (i, 1 << i)
            queue.append((i, 1 << i, 0))
            visited.add(state)

        while queue:
            node, mask, dist = queue.popleft()
            if mask == full_mask:
                return dist
            for nxt in graph[node]:
                new_mask = mask | (1 << nxt)
                state = (nxt, new_mask)
                if state not in visited:
                    visited.add(state)
                    queue.append((nxt, new_mask, dist + 1))
        return -1  # unreachable for a valid connected graph


if __name__ == "__main__":
    sol = Solution()
    assert sol.shortestPathLength([[1, 2, 3], [0], [0], [0]]) == 4
    assert sol.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]) == 4
    assert sol.shortestPathLength([[1], [0]]) == 1
    print("All tests passed.")
