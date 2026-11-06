# 152. Maximum Product Subarray (Medium)
# Given an integer array nums, find a contiguous non-empty subarray that has the
# largest product, and return that product.
# Approach: track both the max and min product ending at the current index, since
# a negative number can flip a very negative running min into the new max.
# Time O(n), Space O(1).

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = cur_max = cur_min = nums[0]
        for num in nums[1:]:
            candidates = (num, cur_max * num, cur_min * num)
            cur_max, cur_min = max(candidates), min(candidates)
            best = max(best, cur_max)
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProduct([2, 3, -2, 4]) == 6
    assert sol.maxProduct([-2, 0, -1]) == 0
    assert sol.maxProduct([-2, 3, -4]) == 24
    print("All tests passed.")
