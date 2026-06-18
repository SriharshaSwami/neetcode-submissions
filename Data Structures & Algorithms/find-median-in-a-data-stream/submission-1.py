class MedianFinder:

    def __init__(self):
#small is MaxHeap, large is MinHeap
        self.small, self.large = [], []
#adding, removing is O(logn) but findMin, findMax operations are O(1)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        if len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val)
        print(self.small, self.large)

    def findMedian(self) -> float:
#if one heap is bigger i.e odd length then return max/min of respective bigger heap
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
#else just avg of max, min 's of each heap
        return (-1 * self.small[0] + self.large[0]) / 2
        