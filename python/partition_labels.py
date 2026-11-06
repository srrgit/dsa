# 763. Partition Labels (Medium)
# Given a string s, partition it into as many parts as possible so that
# each letter appears in at most one part, and return the list of part
# lengths. Each letter must appear only within a single contiguous part.
#
# Approach: greedy. First record the last index at which each letter
# appears. Then scan left to right, extending the current partition's end
# to cover the last occurrence of every letter seen so far; when the scan
# position reaches that end, the partition closes. Time: O(n), Space: O(1)
# extra (26 possible letters).

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}
        lengths = []
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                lengths.append(end - start + 1)
                start = i + 1
        return lengths


if __name__ == "__main__":
    sol = Solution()
    assert sol.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert sol.partitionLabels("eccbbbbdec") == [10]
    print("All test cases passed for 763. Partition Labels")
