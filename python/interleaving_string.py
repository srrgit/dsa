# 97. Interleaving String (Medium)
#
# Given strings s1, s2, s3, determine whether s3 can be formed by
# interleaving s1 and s2 while preserving the relative order of characters
# within each.
#
# Approach: dp[i][j] means "the first i characters of s1 and first j
# characters of s2 can interleave to form the first i+j characters of s3".
# It's true if the last character came from s1 (dp[i-1][j] holds and
# s1[i-1] == s3[i+j-1]) or from s2 (symmetric condition).
# Time: O(m*n). Space: O(m*n) (can be optimized to O(n) with a rolling row).


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # True
    print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # False
    print(sol.isInterleave("", "", ""))                      # True
