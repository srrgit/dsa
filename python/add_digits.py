# 258. Add Digits (Easy)
# Given a non-negative integer num, repeatedly add all its digits together until the result
# has a single digit, and return that digit.
# Approach: this is the digital root, which has a closed-form via modular arithmetic:
# 0 if num == 0, otherwise 1 + (num - 1) % 9. Time O(1), space O(1).


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9


if __name__ == "__main__":
    assert Solution().addDigits(38) == 2
    assert Solution().addDigits(0) == 0
    assert Solution().addDigits(9999) == 9
    print("All tests passed.")
