# 986. Interval List Intersections (Medium)
# Given two lists of disjoint, sorted intervals, return the sorted list of intervals
# representing their pairwise intersections.
# Approach: two-pointer walk over both lists; for the intervals pointed to, compute the overlap
# if any, then advance the pointer belonging to the interval that ends first. Time O(n + m),
# space O(n + m) for the output.

from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        result = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                result.append([start, end])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return result


if __name__ == "__main__":
    assert Solution().intervalIntersection(
        [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]
    ) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    assert Solution().intervalIntersection([[1, 3], [5, 9]], []) == []
    print("All tests passed.")
