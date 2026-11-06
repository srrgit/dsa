# 547. Number of Provinces (Medium)
# Given an n x n adjacency matrix isConnected where isConnected[i][j] == 1 means cities i and j
# are directly connected, return the number of provinces (connected components).
# Approach: union-find (disjoint set union) over the n cities, unioning every directly
# connected pair, then counting the number of distinct roots. Time O(n^2 * alpha(n)), space
# O(n).

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        return len({find(i) for i in range(n)})


if __name__ == "__main__":
    assert Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    print("All tests passed.")
