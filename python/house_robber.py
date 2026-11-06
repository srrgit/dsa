# 198. House Robber (Medium)
# Given non-negative integers representing money stashed in houses arranged in a line, where
# robbing two adjacent houses is not allowed, return the maximum amount that can be robbed.
# Approach: DP with rolling variables: prev2 = best total up to i-2, prev1 = best total up to i-1.
# Time: O(n), Space: O(1).

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        for x in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1


if __name__ == "__main__":
    sol = Solution()
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([2, 7, 9, 3, 1]) == 12
    assert sol.rob([]) == 0
    print("All tests passed.")
