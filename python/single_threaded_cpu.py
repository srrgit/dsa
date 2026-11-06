# 1834. Single-Threaded CPU (Medium)
# Given `tasks` where tasks[i] = [enqueueTime, processingTime], a single-
# threaded CPU processes tasks one at a time, always picking (among tasks
# already available) the one with the shortest processing time, breaking ties
# by the smallest original index; if no task is available it idles until the
# next one arrives. Return the order (original indices) in which tasks are
# processed.
#
# Approach: sort tasks by enqueue time, use a min-heap keyed by (processing
# time, original index) for tasks that have arrived. Advance a simulated
# clock, pushing newly-arrived tasks into the heap, popping the best available
# task, or jumping the clock forward to the next arrival if the heap is empty.
# O(n log n) time, O(n) space.

from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indexed = sorted(range(n), key=lambda i: tasks[i][0])
        heap = []
        result = []
        time = 0
        i = 0
        while len(result) < n:
            while i < n and tasks[indexed[i]][0] <= time:
                idx = indexed[i]
                heapq.heappush(heap, (tasks[idx][1], idx))
                i += 1
            if not heap:
                time = tasks[indexed[i]][0]
                continue
            proc_time, idx = heapq.heappop(heap)
            time += proc_time
            result.append(idx)
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]) == [0, 2, 3, 1]
    assert sol.getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]) == [4, 3, 2, 0, 1]
    print("All tests passed.")
