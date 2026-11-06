# 658. Find K Closest Elements (Medium)
# Given a sorted array arr, an integer k, and a target x, return the k closest integers to x
# in the array, sorted in ascending order (ties broken by the smaller value).
# Approach: binary search for the left boundary of a window of size k such that arr[left] is
# at least as close to x as arr[left + k] is, shrinking the search space until exactly one
# valid left boundary remains. Time O(log(n - k) + k), space O(k).

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = (lo + hi) // 2
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo + k]


if __name__ == "__main__":
    assert Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
    assert Solution().findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
    assert Solution().findClosestElements([1, 1, 2, 3, 4, 5], 4, -1) == [1, 1, 2, 3]
    print("All tests passed.")
