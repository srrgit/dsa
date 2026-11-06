# 852. Peak Index in a Mountain Array (Easy)
#
# A mountain array strictly increases to a peak, then strictly decreases.
# Given such an array, return the index of the peak element.
#
# Approach: binary search on the slope. If arr[mid] < arr[mid+1] we're still
# ascending, so the peak is to the right; otherwise it's at mid or to the left.
# Time: O(log n). Space: O(1).

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    sol = Solution()
    print(sol.peakIndexInMountainArray([0, 1, 0]))        # 1
    print(sol.peakIndexInMountainArray([0, 2, 1, 0]))     # 1
    print(sol.peakIndexInMountainArray([0, 10, 5, 2]))    # 1
