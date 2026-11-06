# 132. Palindrome Partitioning II (Hard)
# Given a string s, partition it so that every substring of the partition is a palindrome, and
# return the minimum number of cuts needed.
# Approach: precompute an is_pal[i][j] table via DP (a substring is a palindrome if its
# endpoints match and the inner substring is a palindrome), then a 1D DP where cuts[i] is the
# minimum cuts needed for s[0:i+1]; for each j <= i with s[j:i+1] a palindrome,
# cuts[i] = min(cuts[i], cuts[j-1] + 1). Time O(n^2), space O(n^2).


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        cuts = [0] * n
        for i in range(n):
            if is_pal[0][i]:
                cuts[i] = 0
                continue
            best = i  # worst case: cut before every character
            for j in range(1, i + 1):
                if is_pal[j][i]:
                    best = min(best, cuts[j - 1] + 1)
            cuts[i] = best
        return cuts[n - 1]


if __name__ == "__main__":
    assert Solution().minCut("aab") == 1
    assert Solution().minCut("a") == 0
    assert Solution().minCut("ab") == 1
    print("All tests passed.")
