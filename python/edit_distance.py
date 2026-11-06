# 72. Edit Distance (Hard)
# Given two strings word1 and word2, return the minimum number of operations (insert a character,
# delete a character, or replace a character) required to convert word1 into word2.
# Approach: classic 2D DP where dp[i][j] = edit distance between word1[:i] and word2[:j]; matching
# characters cost nothing (carry diagonal value), otherwise take 1 + min(insert, delete, replace).
# Time: O(m*n), Space: O(m*n) (reducible to O(n)).

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()
    assert sol.minDistance("horse", "ros") == 3
    assert sol.minDistance("intention", "execution") == 5
    assert sol.minDistance("", "") == 0
    print("All tests passed.")
