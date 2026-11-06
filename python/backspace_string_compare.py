# 844. Backspace String Compare (Easy)
# Given two strings s and t, each containing lowercase letters and '#'
# characters (representing a backspace that deletes the previous
# character, if any), return true if the two strings become equal once
# all backspaces are applied.
#
# Approach: two pointers walking each string from the end, skipping
# characters that get deleted by backspaces on the fly (no extra string
# built). Maintain a skip counter per string: a '#' increments skip; a
# regular character is either consumed by a pending skip or compared.
# Time: O(m + n), Space: O(1).


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_valid_index(string: str, index: int) -> int:
            skip = 0
            while index >= 0:
                if string[index] == "#":
                    skip += 1
                    index -= 1
                elif skip > 0:
                    skip -= 1
                    index -= 1
                else:
                    break
            return index

        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = next_valid_index(s, i)
            j = next_valid_index(t, j)
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.backspaceCompare("ab#c", "ad#c") is True
    assert sol.backspaceCompare("ab##", "c#d#") is True
    assert sol.backspaceCompare("a#c", "b") is False
    print("All test cases passed for 844. Backspace String Compare")
