# 322. Coin Change (Medium)
# Given an array of coin denominations and a target amount, return the fewest
# number of coins needed to make up that amount, or -1 if it cannot be made.
# Approach: bottom-up dynamic programming; dp[a] = min coins to make amount a,
# dp[0] = 0, dp[a] = min(dp[a - c] + 1) over coins c <= a. Time O(n * amount),
# Space O(amount).

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a and dp[a - c] + 1 < dp[a]:
                    dp[a] = dp[a - c] + 1
        return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1], 0) == 0
    print("All tests passed.")
