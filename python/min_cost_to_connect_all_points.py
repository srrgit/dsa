# 1584. Min Cost to Connect All Points (Medium)
# Given points on a 2D plane, the cost to connect two points is their Manhattan
# distance. Return the minimum total cost to connect all points so the graph is
# connected (a minimum spanning tree).
#
# Approach: Prim's algorithm. Keep a min-distance array to the growing tree and
# repeatedly pick the closest unvisited point. O(n^2) time, O(n) space, which is
# fine since n <= 1000 and the graph is dense (complete graph).

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        in_mst = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        total = 0

        for _ in range(n):
            u = -1
            for v in range(n):
                if not in_mst[v] and (u == -1 or min_dist[v] < min_dist[u]):
                    u = v
            in_mst[u] = True
            total += min_dist[u]
            for v in range(n):
                if not in_mst[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < min_dist[v]:
                        min_dist[v] = dist
        return total


if __name__ == "__main__":
    sol = Solution()
    assert sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert sol.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18
    assert sol.minCostConnectPoints([[0, 0]]) == 0
    print("All tests passed.")
