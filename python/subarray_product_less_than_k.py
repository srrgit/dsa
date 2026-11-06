# 713. Subarray Product Less Than K (Medium)
# Given an array of positive integers `nums` and an integer `k`, return the
# number of contiguous subarrays where the product of all elements is strictly
# less than k.
#
# Approach: sliding window. Expand the right pointer, multiplying into a
# running product; whenever the product is >= k, shrink from the left
# (dividing out) until it's valid again. Each valid window of length L ending
# at `right` contributes L new subarrays (all suffixes of that window ending
# at right). O(n) time, O(1) space.

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        product = 1
        count = 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += right - left + 1
        return count


if __name__ == "__main__":
    sol = Solution()
    assert sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
    assert sol.numSubarrayProductLessThanK([1, 2, 3], 0) == 0
    print("All tests passed.")
