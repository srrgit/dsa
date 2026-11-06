# 44. Wildcard Matching (Hard)
# Given an input string s and a pattern p containing '?' (matches any single character)
# and '*' (matches any sequence of characters, including empty), return whether p matches
# s entirely.
# Approach: 2D dynamic programming where dp[i][j] means s[:i] matches p[:j]. '*' inherits
# from dp[i-1][j] (consume one more char of s) or dp[i][j-1] (match the empty sequence).
# Time O(m*n), space O(m*n).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False
        return dp[m][n]


if __name__ == "__main__":
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "*") == True
    assert Solution().isMatch("cb", "?a") == False
    assert Solution().isMatch("adceb", "*a*b") == True
    print("All tests passed.")
