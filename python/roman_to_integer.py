# 13. Roman to Integer (Easy)
# Given a Roman numeral string, convert it to its integer value. Roman
# numerals use subtractive notation in certain cases (e.g. IV = 4,
# IX = 9).
#
# Approach: map each symbol to its value and scan left to right, adding
# the current symbol's value, but subtracting it instead whenever it is
# smaller than the symbol immediately following it (the subtractive
# case). Time: O(n), Space: O(1).


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        n = len(s)
        for i in range(n):
            value = values[s[i]]
            if i + 1 < n and value < values[s[i + 1]]:
                total -= value
            else:
                total += value
        return total


if __name__ == "__main__":
    sol = Solution()
    assert sol.romanToInt("III") == 3
    assert sol.romanToInt("LVIII") == 58
    assert sol.romanToInt("MCMXCIV") == 1994
    print("All test cases passed for 13. Roman to Integer")
