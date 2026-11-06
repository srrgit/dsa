# 647. Palindromic Substrings (Medium)
# Given a string s, return the number of palindromic substrings in it
# (different positions counted separately even if the substring text
# repeats).
#
# Approach: expand around center. For each of the 2n - 1 possible centers
# (each single character, and each gap between two characters for
# even-length palindromes), expand outward while the characters match and
# count each valid expansion. Time: O(n^2), Space: O(1).


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(left: int, right: int) -> int:
            local = 0
            while left >= 0 and right < n and s[left] == s[right]:
                local += 1
                left -= 1
                right += 1
            return local

        for center in range(n):
            count += expand(center, center)      # odd length
            count += expand(center, center + 1)   # even length
        return count


if __name__ == "__main__":
    sol = Solution()
    assert sol.countSubstrings("abc") == 3
    assert sol.countSubstrings("aaa") == 6
    assert sol.countSubstrings("a") == 1
    print("All test cases passed for 647. Palindromic Substrings")
