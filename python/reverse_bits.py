# 190. Reverse Bits (Easy)
# Given a 32-bit unsigned integer, return the integer obtained by reversing the order of its
# bits.
# Approach: iterate over all 32 bit positions, shifting the result left and appending the
# lowest bit of n each time. Time O(32) = O(1), space O(1).


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result


if __name__ == "__main__":
    assert Solution().reverseBits(0b00000010100101000001111010011100) == 964176192
    assert Solution().reverseBits(0b11111111111111111111111111111101) == 3221225471
    print("All tests passed.")
