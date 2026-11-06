# 17. Letter Combinations of a Phone Number (Medium)
# Given a string of digits 2-9, return all possible letter combinations
# that the number could represent on a traditional phone keypad, in any
# order.
#
# Approach: backtracking. For each digit, branch over the letters it maps
# to, building up a partial combination; when the combination's length
# equals the number of digits, record it. Time: O(4^n * n) worst case
# (digit 7 and 9 map to 4 letters each), Space: O(n) recursion depth plus
# output size.

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }

        result = []
        path = []

        def backtrack(index: int) -> None:
            if index == len(digits):
                result.append("".join(path))
                return
            for letter in mapping[digits[index]]:
                path.append(letter)
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.letterCombinations("23")) == sorted(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )
    assert sol.letterCombinations("") == []
    assert sol.letterCombinations("2") == ["a", "b", "c"]
    print("All test cases passed for 17. Letter Combinations of a Phone Number")
