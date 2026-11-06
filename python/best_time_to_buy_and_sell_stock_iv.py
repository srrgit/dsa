# 188. Best Time to Buy and Sell Stock IV (Hard)
# Given daily stock `prices` and an integer `k`, find the maximum profit from
# at most `k` buy-sell transactions (cannot hold more than one share at a
# time, must sell before buying again).
#
# Approach: DP over (transaction index, holding state). hold[t] = max profit
# after at most t transactions while currently holding a share; cash[t] = max
# profit after at most t completed transactions while not holding. Transition
# for each price: hold[t] = max(hold[t], cash[t-1] - price); cash[t] =
# max(cash[t], hold[t] + price). O(n*k) time, O(k) space.

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        k = min(k, n // 2)  # more transactions than n//2 can't help
        cash = [0] * (k + 1)
        hold = [float('-inf')] * (k + 1)

        for price in prices:
            for t in range(1, k + 1):
                hold[t] = max(hold[t], cash[t - 1] - price)
                cash[t] = max(cash[t], hold[t] + price)

        return cash[k]


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit(2, [2, 4, 1]) == 2
    assert sol.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7
    assert sol.maxProfit(1, [1, 2]) == 1
    print("All tests passed.")
