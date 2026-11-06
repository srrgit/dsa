# 214. Shortest Palindrome (Hard)
# Given a string `s`, you may add characters only in front of it. Return the
# shortest palindrome you can produce this way.
#
# Approach: we need the longest prefix of `s` that is itself a palindrome;
# reversing the remaining suffix and prepending it gives the answer. Build the
# combined string s + '#' + reverse(s) and run the KMP failure-function
# algorithm on it; the value at the last position tells us the length of the
# longest prefix of s that matches a suffix of reverse(s), i.e. the longest
# palindromic prefix of s. O(n) time, O(n) space.


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        rev = s[::-1]
        combined = s + '#' + rev
        n = len(combined)
        fail = [0] * n
        k = 0
        for i in range(1, n):
            while k > 0 and combined[i] != combined[k]:
                k = fail[k - 1]
            if combined[i] == combined[k]:
                k += 1
            fail[i] = k

        longest_pal_prefix = fail[-1]
        to_add = rev[:len(s) - longest_pal_prefix]
        return to_add + s


if __name__ == "__main__":
    sol = Solution()
    assert sol.shortestPalindrome("aacecaaa") == "aaacecaaa"
    assert sol.shortestPalindrome("abcd") == "dcbabcd"
    assert sol.shortestPalindrome("") == ""
    print("All tests passed.")
