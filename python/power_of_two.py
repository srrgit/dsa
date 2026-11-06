# 231. Power of Two (Easy)
# Given an integer n, return True if it is a power of two.
# Approach: a positive power of two has exactly one bit set in its binary representation, so for
# n > 0, n & (n - 1) == 0 if and only if n is a power of two.
# Time: O(1), Space: O(1).

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPowerOfTwo(1) is True
    assert sol.isPowerOfTwo(16) is True
    assert sol.isPowerOfTwo(3) is False
    assert sol.isPowerOfTwo(0) is False
    print("All tests passed.")
