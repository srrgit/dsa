# 210. Course Schedule II (Medium)
# Given `numCourses` and a list of prerequisite pairs [a, b] meaning you must
# take b before a, return an ordering of all courses that satisfies every
# prerequisite, or an empty array if no valid ordering (cycle) exists.
#
# Approach: Kahn's algorithm (BFS topological sort) using in-degree counts and
# an adjacency list. O(V + E) time, O(V + E) space.

from typing import List
from collections import deque, defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return order if len(order) == numCourses else []


if __name__ == "__main__":
    sol = Solution()
    assert sol.findOrder(2, [[1, 0]]) == [0, 1]
    result = sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert result.index(0) < result.index(1) < result.index(3)
    assert result.index(0) < result.index(2) < result.index(3)
    assert sol.findOrder(1, []) == [0]
    print("All tests passed.")
