# 1319. Number of Operations to Make Network Connected (Medium)
# Given n computers and a list of connections (direct cables between pairs), return the
# minimum number of cable moves needed to make all computers connected, or -1 if there
# are not enough cables to do it.
# Approach: union-find to count connected components; it's impossible if there are fewer
# than n-1 edges total, otherwise the answer is (number of components - 1), since each
# extra redundant cable can be moved to join two components. Time O(n + E), space O(n).

from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for a, b in connections:
            union(a, b)

        components = len({find(i) for i in range(n)})
        return components - 1


if __name__ == "__main__":
    assert Solution().makeConnected(4, [[0, 1], [0, 2], [1, 2]]) == 1
    assert Solution().makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]) == 2
    assert Solution().makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]) == -1
    print("All tests passed.")
