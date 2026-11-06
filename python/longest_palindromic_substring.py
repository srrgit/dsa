# 5. Longest Palindromic Substring (Medium)
# Given a string s, return the longest palindromic substring of s.
# Approach: expand around every possible center (both single-character centers
# for odd-length palindromes and between-character centers for even-length ones),
# tracking the longest palindrome found. Time O(n^2), Space O(1).


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        best = ""
        for i in range(len(s)):
            odd = expand(i, i)
            if len(odd) > len(best):
                best = odd
            even = expand(i, i + 1)
            if len(even) > len(best):
                best = even
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome("babad") in ("bab", "aba")
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("a") == "a"
    print("All tests passed.")
