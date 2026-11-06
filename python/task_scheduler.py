# 621. Task Scheduler (Medium)
# Given a list of CPU tasks (characters) and a cooldown n, where the same
# task must be separated by at least n intervals (idle slots allowed),
# return the minimum number of intervals needed to finish all tasks.
#
# Approach: greedy counting formula. Let max_freq be the highest frequency
# among tasks and max_count the number of distinct tasks that reach that
# frequency. The most frequent task(s) dictate (max_freq - 1) full
# "chunks" of size (n + 1), plus a final chunk containing all tasks tied
# for max frequency. The answer is max(len(tasks), (max_freq - 1) * (n + 1)
# + max_count). Time: O(len(tasks)), Space: O(1) (26 possible task types).

from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = sum(1 for v in freq.values() if v == max_freq)
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)


if __name__ == "__main__":
    sol = Solution()
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert sol.leastInterval(
        ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
    ) == 16
    print("All test cases passed for 621. Task Scheduler")
