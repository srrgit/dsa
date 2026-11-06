# 392. Is Subsequence (Easy)
# Given two strings s and t, return true if s is a subsequence of t.
# Approach: two pointers scanning t once, advancing the s pointer whenever characters match.
# Time O(n) where n = len(t), space O(1).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n = len(s)
        if n == 0:
            return True
        for ch in t:
            if i < n and ch == s[i]:
                i += 1
                if i == n:
                    return True
        return i == n


if __name__ == "__main__":
    assert Solution().isSubsequence("abc", "ahbgdc") == True
    assert Solution().isSubsequence("axc", "ahbgdc") == False
    assert Solution().isSubsequence("", "ahbgdc") == True
    print("All tests passed.")
