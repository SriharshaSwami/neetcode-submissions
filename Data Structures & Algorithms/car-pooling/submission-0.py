class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        minHeap = [] 
        heapq.heapify(minHeap)

        curPass = 0
        for trip in trips:
            nextPass, start, end = trip
            while minHeap and minHeap[0][0] <= start:
                [en, freePass] = heapq.heappop(minHeap)
                curPass -= freePass

            curPass += nextPass
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, [end, nextPass])
        
        return True