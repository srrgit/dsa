# 67. Add Binary (Easy)
# Given two binary strings a and b, return their sum as a binary string.
# Approach: simulate binary addition from the least significant bit using a carry,
# building the result in reverse. Time O(max(len(a), len(b))), space O(max(len(a), len(b))).

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return ''.join(reversed(result))


if __name__ == "__main__":
    assert Solution().addBinary("11", "1") == "100"
    assert Solution().addBinary("1010", "1011") == "10101"
    print("All tests passed.")
