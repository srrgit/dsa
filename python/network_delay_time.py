# 743. Network Delay Time (Medium)
# Given a network of n nodes labeled 1..n and travel times as directed
# weighted edges (times = [[u, v, w], ...]), and a starting node k, return
# the minimum time for all n nodes to receive a signal sent from node k.
# Return -1 if it is impossible for all nodes to receive the signal.
#
# Approach: Dijkstra's algorithm with a min-heap. Repeatedly pop the
# closest unvisited node, relax its outgoing edges, and track the best
# known distance to each node. The answer is the maximum distance among all
# reachable nodes (or -1 if not all nodes were reached).
# Time: O(E log V), Space: O(V + E).

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}
        heap = [(0, k)]
        while heap:
            d, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = d
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(heap, (d + weight, neighbor))

        if len(dist) != n:
            return -1
        return max(dist.values())


if __name__ == "__main__":
    sol = Solution()
    assert sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert sol.networkDelayTime([[1, 2, 1]], 2, 1) == 1
    assert sol.networkDelayTime([[1, 2, 1]], 2, 2) == -1
    print("All test cases passed for 743. Network Delay Time")
