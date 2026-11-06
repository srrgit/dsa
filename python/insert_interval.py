# 57. Insert Interval (Medium)
# Given a set of non-overlapping intervals sorted by start, and a new interval,
# insert the new interval merging as needed, and return the resulting sorted,
# non-overlapping list of intervals.
# Approach: linear scan in three phases — copy all intervals that end strictly
# before the new interval starts, merge all intervals that overlap the new
# interval into it, then copy the remaining intervals. Time O(n), Space O(n).

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)
        start, end = newInterval

        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])

        while i < n:
            result.append(intervals[i])
            i += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert sol.insert(
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    ) == [[1, 2], [3, 10], [12, 16]]
    assert sol.insert([], [5, 7]) == [[5, 7]]
    print("All tests passed.")
