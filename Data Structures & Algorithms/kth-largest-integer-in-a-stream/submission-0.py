class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        self.k = k

    def add(self, val: int) -> int:
        # first just push the val into heap
        heapq.heappush(self.minHeap, val)

        # now remove unwanted small numbers, so min becomes the k th largest
        while(len(self.minHeap) > self.k):
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
