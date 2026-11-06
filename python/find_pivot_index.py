# 724. Find Pivot Index (Easy)
# Given an array of integers nums, return the leftmost pivot index where the sum of all
# numbers strictly to the left equals the sum of all numbers strictly to the right, or -1.
# Approach: compute the total sum, then scan left to right tracking a running left sum
# and comparing against (total - leftSum - nums[i]). Time O(n), space O(1).

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num
        return -1


if __name__ == "__main__":
    assert Solution().pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert Solution().pivotIndex([1, 2, 3]) == -1
    assert Solution().pivotIndex([2, 1, -1]) == 0
    print("All tests passed.")
