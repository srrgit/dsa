# 1288. Remove Covered Intervals (Medium)
# Given a list of intervals, remove all intervals that are covered by another
# interval in the list ([a, b) is covered by [c, d) if c <= a and b <= d), and
# return the number of remaining intervals.
#
# Approach: sort intervals by start ascending, and by end descending for ties
# (so that if two intervals share a start, the longer one comes first and
# automatically covers the shorter one). Then sweep, keeping track of the
# furthest `end` seen among kept intervals; an interval is covered iff its end
# <= that furthest end. O(n log n) time, O(1) extra space (ignoring the sort).

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda iv: (iv[0], -iv[1]))
        count = 0
        furthest_end = -1
        for start, end in intervals:
            if end > furthest_end:
                count += 1
                furthest_end = end
        return count


if __name__ == "__main__":
    sol = Solution()
    assert sol.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]) == 2
    assert sol.removeCoveredIntervals([[1, 4], [2, 3]]) == 1
    print("All tests passed.")
