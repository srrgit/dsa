# 787. Cheapest Flights Within K Stops (Medium)
# Given n cities, a list of flights [from, to, price], a source, a destination, and a maximum
# number of stops k, return the cheapest price to travel from src to dst using at most k
# stops (i.e., at most k+1 edges), or -1 if impossible.
# Approach: Bellman-Ford relaxed for exactly k+1 rounds, using a snapshot of distances each
# round so updates within the same round don't chain beyond the stop limit.
# Time O(k * E), space O(n).

from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        INF = float("inf")
        dist = [INF] * n
        dist[src] = 0

        for _ in range(k + 1):
            new_dist = dist[:]
            for u, v, price in flights:
                if dist[u] != INF and dist[u] + price < new_dist[v]:
                    new_dist[v] = dist[u] + price
            dist = new_dist

        return -1 if dist[dst] == INF else dist[dst]


if __name__ == "__main__":
    assert Solution().findCheapestPrice(
        4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1
    ) == 700
    assert Solution().findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1
    ) == 200
    assert Solution().findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0
    ) == 500
    print("All tests passed.")
