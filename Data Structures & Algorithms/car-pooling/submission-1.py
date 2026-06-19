class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # first sort trips acc to start time
        trips.sort(key = lambda x: x[1])
        minHeap = [] # stores [dest, passengers]
        heapq.heapify(minHeap)

        curPass = 0
        for trip in trips:
        # get the next trip details
            nextPass, start, end = trip
        # now before trying to fit the new passengers, check for any passengers can be dropped
        # if the least destination from the minHeap is reached, drop off those passengers
            while minHeap and minHeap[0][0] <= start:
                [en, freePass] = heapq.heappop(minHeap)
                curPass -= freePass
        # after trying to drop off, now add the new passengers
            curPass += nextPass
        # after adding new passengers, check if capacity exceeded, if yes immediately return False
            if curPass > capacity:
                return False
        # if we addded new passengers, we record them in minHeap for later until their drop off
            heapq.heappush(minHeap, [end, nextPass])
        # return True if no conflicts with capacity occured
        return True