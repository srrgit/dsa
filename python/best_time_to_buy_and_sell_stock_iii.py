# 123. Best Time to Buy and Sell Stock III (Hard)
# Given an array prices where prices[i] is the stock price on day i, find
# the maximum profit achievable with at most two transactions (you must
# sell before buying again).
#
# Approach: track four running states while scanning once: buy1 (max cash
# after first buy, i.e. -price so far), sell1 (max profit after first
# sell), buy2 (max cash after second buy using profit from sell1), sell2
# (max profit after second sell). Update them in order each day.
# Time: O(n), Space: O(1).

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy1 = buy2 = float("-inf")
        sell1 = sell2 = 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    print("All test cases passed for 123. Best Time to Buy and Sell Stock III")
