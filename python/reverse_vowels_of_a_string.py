# 345. Reverse Vowels of a String (Easy)
# Given a string s, reverse only the vowels (a, e, i, o, u, case-insensitive) in place,
# leaving all other characters in their original positions.
# Approach: two pointers from both ends of the string; swap when both point at vowels,
# otherwise advance the pointer not on a vowel. Time O(n), space O(n) for the char list.


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)
        left, right = 0, len(chars) - 1

        while left < right:
            if chars[left] not in vowels:
                left += 1
            elif chars[right] not in vowels:
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return "".join(chars)


if __name__ == "__main__":
    assert Solution().reverseVowels("hello") == "holle"
    assert Solution().reverseVowels("leetcode") == "leotcede"
    print("All tests passed.")
