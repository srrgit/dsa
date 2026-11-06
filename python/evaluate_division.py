# 399. Evaluate Division (Medium)
# Given equations like a/b = 2.0 as pairs with values, and queries like a/c, return the
# evaluated value for each query, or -1.0 if it cannot be determined.
# Approach: build a weighted directed graph (a -> b with weight value, b -> a with
# weight 1/value) and run DFS from the query's numerator to the denominator, multiplying
# edge weights along the path. Time O((V+E) * Q), space O(V+E).

from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                      queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1.0 / v

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited.add(src)
            for neighbor, weight in graph[src].items():
                if neighbor in visited:
                    continue
                result = dfs(neighbor, dst, visited)
                if result != -1.0:
                    return weight * result
            return -1.0

        return [dfs(a, b, set()) for a, b in queries]


if __name__ == "__main__":
    eqs = [["a", "b"], ["b", "c"]]
    vals = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    result = Solution().calcEquation(eqs, vals, queries)
    expected = [6.0, 0.5, -1.0, 1.0, -1.0]
    assert all(abs(r - e) < 1e-5 for r, e in zip(result, expected))
    print("All tests passed.")
