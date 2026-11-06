# 441. Arranging Coins (Easy)
# You have n coins to form a staircase, where the k-th row must have exactly k coins; the last
# row may be incomplete. Return the number of complete rows that can be formed.
# Approach: binary search for the largest k such that k*(k+1)/2 <= n (closed-form math also
# works, but binary search avoids floating-point precision issues). Time O(log n), space O(1).


class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if mid * (mid + 1) // 2 <= n:
                lo = mid
            else:
                hi = mid - 1
        return lo


if __name__ == "__main__":
    assert Solution().arrangeCoins(5) == 2
    assert Solution().arrangeCoins(8) == 3
    assert Solution().arrangeCoins(1) == 1
    print("All tests passed.")
