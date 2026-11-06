# 767. Reorganize String (Medium)
# Given a string s, rearrange its characters so that no two adjacent characters are the
# same, returning any valid rearrangement, or an empty string if impossible.
# Approach: count character frequencies, push them into a max-heap by frequency, and
# greedily place the most frequent remaining character, holding back the previously
# placed character for one step so it can't be placed again immediately. Time
# O(n log k) where k is the alphabet size, space O(k).

from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = Counter(s)
        max_count = max(counts.values())
        if max_count > (n + 1) // 2:
            return ""

        heap = [(-cnt, ch) for ch, cnt in counts.items()]
        heapq.heapify(heap)

        result = []
        prev_cnt, prev_ch = 0, ''
        while heap:
            cnt, ch = heapq.heappop(heap)
            result.append(ch)
            cnt += 1  # one occurrence used (cnt is negative, so this increments toward 0)
            if prev_cnt < 0:
                heapq.heappush(heap, (prev_cnt, prev_ch))
            prev_cnt, prev_ch = cnt, ch

        return ''.join(result)


def is_valid_reorg(original: str, result: str) -> bool:
    if len(result) != len(original):
        return False
    if sorted(result) != sorted(original):
        return False
    return all(result[i] != result[i + 1] for i in range(len(result) - 1))


if __name__ == "__main__":
    assert is_valid_reorg("aab", Solution().reorganizeString("aab"))
    assert Solution().reorganizeString("aaab") == ""  # impossible: 'a' needs 3 of 4 slots
    result = Solution().reorganizeString("aaabc")
    assert is_valid_reorg("aaabc", result)
    print("All tests passed.")
