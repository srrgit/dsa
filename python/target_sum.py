# 494. Target Sum (Medium)
# Given an integer array nums and an integer target, assign a '+' or '-'
# sign to each number and count how many ways there are to make the sum of
# the resulting expression equal to target.
#
# Approach: DFS with memoization on (index, current_sum). Since nums
# values and the number of elements are small, cache results keyed by
# (index, running total) to avoid recomputation of overlapping subproblems.
# Time: O(n * range_of_sums), Space: O(n * range_of_sums).

from functools import lru_cache
from typing import List, Tuple


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def dfs(i: int, total: int) -> int:
            if i == n:
                return 1 if total == target else 0
            return dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])

        result = dfs(0, 0)
        dfs.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
    assert sol.findTargetSumWays([1], 1) == 1
    assert sol.findTargetSumWays([1, 0], 1) == 2
    print("All test cases passed for 494. Target Sum")
