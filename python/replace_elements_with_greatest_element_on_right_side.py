# 1299. Replace Elements with Greatest Element on Right Side (Easy)
# Given an array `arr`, replace every element with the greatest element among
# the elements to its right, and replace the last element with -1.
#
# Approach: traverse from right to left, keeping track of the max seen so far
# and writing it before updating the max with the current (original) value.
# O(n) time, O(1) extra space (besides the output array).

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [0] * len(arr)
        max_so_far = -1
        for i in range(len(arr) - 1, -1, -1):
            result[i] = max_so_far
            max_so_far = max(max_so_far, arr[i])
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
    assert sol.replaceElements([400]) == [-1]
    print("All tests passed.")
