# 685. Redundant Connection II (Hard)
# A rooted tree on n nodes had one extra directed edge added, producing n edges for n nodes.
# Given the edges in input order, find the one edge that can be removed so that the remaining
# n-1 edges form a valid rooted tree (every node has exactly one parent, no cycles). If
# several edges could be removed, return the one that occurs last in the input.
# Approach: first scan for a node with two parents (two edges pointing to the same child) --
# call them candidate1 (earlier) and candidate2 (later). If found, tentatively remove
# candidate2 and union-find the rest of the edges: if that still forms a cycle, candidate2
# wasn't the real problem, so return candidate1; otherwise return candidate2. If no node has
# two parents, the extra edge purely created a cycle, found directly via union-find.
# Time O(n) (union-find with path compression), space O(n).

from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent_of = [0] * (n + 1)
        candidate1 = candidate2 = None

        for u, v in edges:
            if parent_of[v] != 0:
                candidate1 = [parent_of[v], v]
                candidate2 = [u, v]
                break
            parent_of[v] = u

        uf_parent = list(range(n + 1))

        def find(x: int) -> int:
            while uf_parent[x] != x:
                uf_parent[x] = uf_parent[uf_parent[x]]
                x = uf_parent[x]
            return x

        for u, v in edges:
            if candidate2 is not None and [u, v] == candidate2:
                continue
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return candidate1 if candidate1 is not None else [u, v]
            uf_parent[root_v] = root_u

        return candidate2


if __name__ == "__main__":
    assert Solution().findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert Solution().findRedundantDirectedConnection(
        [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
    ) == [4, 1]
    print("All tests passed.")
