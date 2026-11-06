# 69. Sqrt(x) (Easy)
# Given a non-negative integer x, return the integer square root of x (the square root
# rounded down to the nearest integer), without using built-in exponent/sqrt operators.
# Approach: binary search over candidate answers in [0, x] for the largest value whose square
# does not exceed x. Time O(log x), space O(1).


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        lo, hi = 1, x // 2
        ans = 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid <= x:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans


if __name__ == "__main__":
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
    assert Solution().mySqrt(0) == 0
    assert Solution().mySqrt(1) == 1
    print("All tests passed.")
