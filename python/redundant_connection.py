# 684. Redundant Connection (Medium)
# A graph started as a tree with n nodes and one extra edge was added,
# creating exactly one cycle. Given edges as [u, v] pairs, return the edge
# that can be removed to restore the tree; if multiple answers exist,
# return the one that occurs last in the input.
#
# Approach: Union-Find (disjoint set union) with path compression and
# union by rank. Process edges in order; the first edge whose two
# endpoints already belong to the same component is the redundant one.
# Time: O(n) with near-constant-time find/union operations, Space: O(n).

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> bool:
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False
            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []


if __name__ == "__main__":
    sol = Solution()
    assert sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    print("All test cases passed for 684. Redundant Connection")
