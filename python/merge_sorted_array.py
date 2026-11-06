# 88. Merge Sorted Array (Easy)
# nums1 and nums2 are sorted non-decreasing arrays, with nums1 having extra
# trailing space (length m + n) to hold the merged result. Merge nums2 into
# nums1 in-place so it becomes one sorted array of length m + n.
#
# Approach: merge from the back. Use three pointers: i for the last real
# element of nums1, j for the last element of nums2, and k for the last
# slot of nums1. Place the larger of nums1[i]/nums2[j] at nums1[k] and
# move pointers inward. This avoids overwriting unread values.
# Time: O(m + n), Space: O(1).

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    sol.merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums2 = [1]
    sol.merge(nums2, 1, [], 0)
    assert nums2 == [1]

    nums3 = [0]
    sol.merge(nums3, 0, [1], 1)
    assert nums3 == [1]

    print("All test cases passed for 88. Merge Sorted Array")
