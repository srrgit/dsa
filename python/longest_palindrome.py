# 409. Longest Palindrome (Easy)
# Given a string s consisting of lowercase and/or uppercase letters, return the length of the
# longest palindrome that can be built by rearranging the letters (case-sensitive).
# Approach: count character frequencies; every character contributes floor(count / 2) * 2 to
# the palindrome length (pairs on each side), and if any character has an odd count, one
# single character can sit in the exact middle, adding 1. Time O(n), space O(1) (bounded
# alphabet).

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd = False
        for count in counts.values():
            length += (count // 2) * 2
            if count % 2 == 1:
                has_odd = True
        return length + 1 if has_odd else length


if __name__ == "__main__":
    assert Solution().longestPalindrome("abccccdd") == 7
    assert Solution().longestPalindrome("a") == 1
    assert Solution().longestPalindrome("bb") == 2
    print("All tests passed.")
