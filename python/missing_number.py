# 268. Missing Number (Easy)
# Given an array nums containing n distinct numbers taken from the range [0, n], return the one
# number in that range that is missing from the array.
# Approach: the sum of all integers in [0, n] equals n*(n+1)//2; subtracting the actual sum of
# nums from this expected sum yields the missing number.
# Time: O(n), Space: O(1).

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        return expected - sum(nums)


if __name__ == "__main__":
    sol = Solution()
    assert sol.missingNumber([3, 0, 1]) == 2
    assert sol.missingNumber([0, 1]) == 2
    assert sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    print("All tests passed.")
