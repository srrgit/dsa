# 53. Maximum Subarray (Easy)
# Given an integer array nums, find the subarray with the largest sum and return that sum.
# Approach: Kadane's algorithm, tracking best running sum ending at the current index.
# Time: O(n), Space: O(1).

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        curr = nums[0]
        for x in nums[1:]:
            curr = max(x, curr + x)
            best = max(best, curr)
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
    print("All tests passed.")
