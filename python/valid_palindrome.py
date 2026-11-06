# 125. Valid Palindrome (Easy)
# Given a string s, return True if, after converting all uppercase letters to lowercase and
# removing all non-alphanumeric characters, it reads the same forward and backward.
# Approach: two pointers from both ends, skipping non-alphanumeric characters as they move inward.
# Time: O(n), Space: O(1).

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
    assert sol.isPalindrome("race a car") is False
    assert sol.isPalindrome(" ") is True
    print("All tests passed.")
