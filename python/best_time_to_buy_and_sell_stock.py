# 121. Best Time to Buy and Sell Stock (Easy)
# Given an array prices where prices[i] is the stock price on day i, find the
# maximum profit achievable by buying on one day and selling on a later day
# (or 0 if no profit is possible).
# Approach: track the minimum price seen so far while scanning left to right and
# keep the best (price - min_so_far). Time O(n), Space O(1).

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0
        for price in prices:
            min_price = min(min_price, price)
            best = max(best, price - min_price)
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([2, 4, 1]) == 2
    print("All tests passed.")
