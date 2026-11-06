# 315. Count of Smaller Numbers After Self (Hard)
# Given an integer array nums, return an array counts where counts[i] is the number of
# elements to the right of nums[i] that are smaller than nums[i].
# Approach: coordinate-compress the values and use a Binary Indexed Tree (Fenwick tree),
# processing nums from right to left: query the count of smaller ranks already inserted,
# then insert the current rank. Time O(n log n), space O(n).

from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        sorted_unique = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}  # 1-indexed for BIT
        n = len(sorted_unique)
        tree = [0] * (n + 1)

        def update(i: int) -> None:
            while i <= n:
                tree[i] += 1
                i += i & (-i)

        def query(i: int) -> int:
            total = 0
            while i > 0:
                total += tree[i]
                i -= i & (-i)
            return total

        result = [0] * len(nums)
        for idx in range(len(nums) - 1, -1, -1):
            r = rank[nums[idx]]
            result[idx] = query(r - 1)
            update(r)
        return result


if __name__ == "__main__":
    assert Solution().countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]
    assert Solution().countSmaller([-1]) == [0]
    assert Solution().countSmaller([-1, -1]) == [0, 0]
    print("All tests passed.")
