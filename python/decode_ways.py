# 91. Decode Ways (Medium)
# A message containing letters A-Z is encoded to numbers using the mapping A->1 ... Z->26.
# Given a string s containing only digits, return the number of ways to decode it.
# Approach: dynamic programming over positions, tracking the number of ways using the last
# one or two digits, rolling two variables. Time O(n), space O(1).

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        prev2, prev1 = 1, 1  # dp[i-2], dp[i-1]
        for i in range(1, n):
            curr = 0
            if s[i] != '0':
                curr += prev1
            two_digit = int(s[i - 1:i + 1])
            if 10 <= two_digit <= 26:
                curr += prev2
            if curr == 0:
                return 0
            prev2, prev1 = prev1, curr
        return prev1


if __name__ == "__main__":
    assert Solution().numDecodings("12") == 2
    assert Solution().numDecodings("226") == 3
    assert Solution().numDecodings("06") == 0
    print("All tests passed.")
