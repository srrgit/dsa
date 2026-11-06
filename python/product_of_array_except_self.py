# 238. Product of Array Except Self (Medium)
# Given an integer array nums, return an array answer such that answer[i] equals the product of
# all elements of nums except nums[i], without using the division operator.
# Approach: compute prefix products from the left and suffix products from the right in two
# separate passes, multiplying them together into the output array.
# Time: O(n), Space: O(1) extra (excluding the output array).

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


if __name__ == "__main__":
    sol = Solution()
    assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert sol.productExceptSelf([2, 3]) == [3, 2]
    print("All tests passed.")
