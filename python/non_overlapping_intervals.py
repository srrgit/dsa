# 435. Non-overlapping Intervals (Medium)
# Given an array of intervals, return the minimum number of intervals you need to
# remove to make the rest of the intervals non-overlapping.
# Approach: greedy — sort by end time; keep an interval if its start is >= the end
# of the last kept interval, otherwise it must be removed (it conflicts and keeping
# the earlier-ending one maximizes future room). Time O(n log n), Space O(1).

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda iv: iv[1])
        removed = 0
        prev_end = float("-inf")
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                removed += 1
        return removed


if __name__ == "__main__":
    sol = Solution()
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    print("All tests passed.")
