# 122. Best Time to Buy and Sell Stock II (Medium)
# Given an array prices where prices[i] is the stock price on day i, find the maximum
# profit achievable with unlimited buy/sell transactions (no holding more than one share
# at a time).
# Approach: greedily sum every positive day-to-day price increase, which is equivalent to
# capturing every rising segment of the price curve. Time O(n), space O(1).

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


if __name__ == "__main__":
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
    print("All tests passed.")
