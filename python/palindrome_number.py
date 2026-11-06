# 9. Palindrome Number (Easy)
# Given an integer x, return true if x is a palindrome integer, without converting it to
# a string.
# Approach: negative numbers and positive numbers ending in 0 (except 0 itself) can't be
# palindromes; otherwise reverse the second half of the number and compare it to the
# remaining first half. Time O(log10(x)), space O(1).

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10
        return x == reverted or x == reverted // 10


if __name__ == "__main__":
    assert Solution().isPalindrome(121) == True
    assert Solution().isPalindrome(-121) == False
    assert Solution().isPalindrome(10) == False
    print("All tests passed.")
