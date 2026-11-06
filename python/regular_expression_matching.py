# 10. Regular Expression Matching (Hard)
# Given an input string s and a pattern p, implement regular expression matching supporting '.'
# (matches any single character) and '*' (matches zero or more of the preceding element). The
# match must cover the entire input string.
# Approach: 2D DP where dp[i][j] = whether s[:i] matches p[:j]. A '*' is handled by either skipping
# the preceding element+star pair entirely (zero occurrences), or, if the preceding element
# matches s[i-1], consuming one character of s while staying at the same pattern position.
# Time: O(m*n), Space: O(m*n).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == "*" and j >= 2:
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pc = p[j - 1]
                if pc == "*":
                    prev_char = p[j - 2]
                    dp[i][j] = dp[i][j - 2]  # zero occurrences of prev_char
                    if prev_char == "." or prev_char == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    if pc == "." or pc == s[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()
    assert sol.isMatch("aa", "a") is False
    assert sol.isMatch("aa", "a*") is True
    assert sol.isMatch("ab", ".*") is True
    assert sol.isMatch("mississippi", "mis*is*p*.") is False
    print("All tests passed.")
