# 56. Merge Intervals (Medium)
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all
# overlapping intervals and return an array of the non-overlapping intervals that
# cover all the intervals in the input.
# Approach: sort by start; iterate and merge with the last interval in the result
# when it overlaps (current start <= last end). Time O(n log n), Space O(n).

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda iv: iv[0])
        merged = [intervals[0][:]]
        for start, end in intervals[1:]:
            last = merged[-1]
            if start <= last[1]:
                last[1] = max(last[1], end)
            else:
                merged.append([start, end])
        return merged


if __name__ == "__main__":
    sol = Solution()
    assert sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert sol.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert sol.merge([[1, 4]]) == [[1, 4]]
    print("All tests passed.")
