# 70. Climbing Stairs (Easy)
# You are climbing a staircase of n steps, taking either 1 or 2 steps at a time.
# Return the number of distinct ways to climb to the top.
# Approach: this is Fibonacci — ways(n) = ways(n-1) + ways(n-2); iterate with two
# rolling variables instead of recursing. Time O(n), Space O(1).


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    sol = Solution()
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(5) == 8
    print("All tests passed.")
