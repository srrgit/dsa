# 1486. XOR Operation in an Array (Easy)
#
# Given n and start, nums[i] = start + 2*i for i in [0, n-1].
# Return the XOR of all elements of nums.
#
# Approach: generate each value on the fly and XOR it into a running
# accumulator; no need to materialize the array.
# Time: O(n). Space: O(1).


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= (start + 2 * i)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.xorOperation(5, 0))   # 8
    print(sol.xorOperation(4, 3))   # 8
