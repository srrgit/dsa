# 416. Partition Equal Subset Sum (Medium)
# Given an array of positive integers, return True if it can be partitioned into two subsets such
# that the sum of elements in both subsets is equal.
# Approach: if the total sum is odd, it's impossible; otherwise this reduces to a 0/1 subset-sum
# DP for target = total/2, using a boolean array updated right-to-left per item so each number is
# used at most once.
# Time: O(n * target), Space: O(target).

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for x in nums:
            for s in range(target, x - 1, -1):
                if dp[s - x]:
                    dp[s] = True
        return dp[target]


if __name__ == "__main__":
    sol = Solution()
    assert sol.canPartition([1, 5, 11, 5]) is True
    assert sol.canPartition([1, 2, 3, 5]) is False
    assert sol.canPartition([1, 1]) is True
    print("All tests passed.")
