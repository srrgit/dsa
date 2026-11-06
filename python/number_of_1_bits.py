# 191. Number of 1 Bits (Easy)
# Given a 32-bit unsigned integer n, return the number of '1' bits it has (the
# Hamming weight).
# Approach: repeatedly clear the lowest set bit using n &= (n - 1); the number of
# iterations until n becomes 0 equals the number of set bits. Time O(k) where k is
# the number of set bits (at most 32), Space O(1).


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    assert sol.hammingWeight(11) == 3       # 0b1011
    assert sol.hammingWeight(128) == 1      # 0b10000000
    assert sol.hammingWeight(4294967293) == 31  # 0b11111111111111111111111111111101
    print("All tests passed.")
