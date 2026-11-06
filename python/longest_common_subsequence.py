# 1143. Longest Common Subsequence (Medium)
# Given two strings text1 and text2, return the length of their longest
# common subsequence (characters in relative order, not necessarily
# contiguous), or 0 if none exists.
#
# Approach: classic 2D dynamic programming. dp[i][j] = length of LCS of
# text1[:i] and text2[:j]. If the current characters match, extend the
# diagonal result; otherwise take the best of dropping a character from
# either string. Time: O(m * n), Space: O(m * n).


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestCommonSubsequence("abcde", "ace") == 3
    assert sol.longestCommonSubsequence("abc", "abc") == 3
    assert sol.longestCommonSubsequence("abc", "def") == 0
    print("All test cases passed for 1143. Longest Common Subsequence")
