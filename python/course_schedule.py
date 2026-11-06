# 207. Course Schedule (Medium)
# There are numCourses courses labeled 0 to numCourses-1. Given prerequisite pairs
# [a, b] meaning you must take course b before course a, return True if you can
# finish all courses (i.e. the prerequisite graph has no cycle).
# Approach: Kahn's algorithm — build an adjacency list and in-degree counts, then
# repeatedly remove nodes with in-degree 0; if all nodes get removed there is no
# cycle. Time O(V + E), Space O(V + E).

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        visited = 0
        while queue:
            node = queue.popleft()
            visited += 1
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return visited == numCourses


if __name__ == "__main__":
    sol = Solution()
    assert sol.canFinish(2, [[1, 0]]) is True
    assert sol.canFinish(2, [[1, 0], [0, 1]]) is False
    assert sol.canFinish(1, []) is True
    print("All tests passed.")
