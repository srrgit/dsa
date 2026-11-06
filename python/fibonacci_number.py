# 509. Fibonacci Number (Easy)
# Given n, calculate F(n) for the Fibonacci sequence where F(0)=0, F(1)=1, and
# F(n) = F(n-1) + F(n-2) for n > 1.
# Approach: iterative computation with two rolling variables instead of recursion or an
# array. Time O(n), space O(1).

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    assert Solution().fib(2) == 1
    assert Solution().fib(3) == 2
    assert Solution().fib(4) == 3
    print("All tests passed.")
