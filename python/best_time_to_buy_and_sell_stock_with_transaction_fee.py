# 714. Best Time to Buy and Sell Stock with Transaction Fee (Medium)
# Given daily stock `prices` and a constant transaction `fee`, find the max
# profit achievable with unlimited buy/sell transactions, where each completed
# transaction (one buy + one sell) incurs the fee once.
#
# Approach: DP with two running states: `cash` (max profit with no stock held)
# and `hold` (max profit while holding one share). Transition each day:
# cash = max(cash, hold + price - fee); hold = max(hold, cash - price).
# O(n) time, O(1) space.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        cash, hold = 0, -prices[0]
        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8
    assert sol.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6
    print("All tests passed.")
