# 1043. Partition Array for Maximum Sum (Medium)
# Given an integer array `arr` and an integer `k`, partition arr into
# contiguous subarrays of length at most k; after partitioning, each subarray's
# elements are changed to the max value of that subarray. Return the largest
# possible sum of the modified array.
#
# Approach: DP where dp[i] = best achievable sum for arr[:i]. For each i, try
# every partition length L (1..k) ending at i: dp[i] = max over L of dp[i-L] +
# L * max(arr[i-L:i]). O(n*k) time, O(n) space.

from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            cur_max = 0
            best = 0
            for L in range(1, min(k, i) + 1):
                cur_max = max(cur_max, arr[i - L])
                best = max(best, dp[i - L] + cur_max * L)
            dp[i] = best
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3) == 84
    assert sol.maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4) == 83
    assert sol.maxSumAfterPartitioning([1], 1) == 1
    print("All tests passed.")
