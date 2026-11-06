# 295. Find Median from Data Stream (Hard)
# Design a data structure that supports adding integers from a stream and
# efficiently finding the median of all elements added so far.
# Approach: maintain two heaps — a max-heap for the lower half (stored as negated
# values in a min-heap) and a min-heap for the upper half, keeping their sizes
# balanced (differ by at most 1). The median is the top of the larger heap, or the
# average of both tops when sizes are equal. addNum: O(log n), findMedian: O(1).

import heapq


class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (negated), holds the smaller half
        self.large = []  # min-heap, holds the larger half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0

    mf2 = MedianFinder()
    mf2.addNum(6)
    assert mf2.findMedian() == 6.0
    print("All tests passed.")
