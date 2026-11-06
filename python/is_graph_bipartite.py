# 785. Is Graph Bipartite? (Medium)
# Given an undirected graph as an adjacency list, determine whether its nodes can be split
# into two independent sets such that every edge connects a node in one set to a node in the
# other (i.e., the graph is bipartite).
# Approach: BFS/coloring each connected component with two colors; if a neighbor already has
# the same color as the current node, the graph is not bipartite. Time O(V + E), space O(V).

from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n  # 0 = uncolored, 1 or -1 = the two colors

        for start in range(n):
            if color[start] != 0:
                continue
            color[start] = 1
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
        return True


if __name__ == "__main__":
    assert Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False
    assert Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) is True
    print("All tests passed.")
