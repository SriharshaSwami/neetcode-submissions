class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        maxHeap = []
        # add to heap only if counts are usable, use -ve values to simulate maxHeap
        if a: maxHeap.append([-a, 'a'])
        if b: maxHeap.append([-b, 'b'])
        if c: maxHeap.append([-c, 'c'])
        # heapify, it uses the first element in list as criteria for heapify
        heapq.heapify(maxHeap)

        res = ""

        while(maxHeap):
        # get the most frequent ch
            [count, ch] = heapq.heappop(maxHeap)
        # if it is already repeated twice, we can't use it again, so search for other ch
            if res.endswith(ch * 2):
        # if heap is empty, no other ch is available, so stop building res immediately
                if not maxHeap: break
        # else, we get the next most frequent ch and add to the res
                else:
                    [nextCount, nextCh] = heapq.heappop(maxHeap)
                    res += nextCh
                    nextCount += 1
        # if ch is still usable push back into the heap
                    if nextCount:
                        heapq.heappush(maxHeap, [nextCount, nextCh])
        # if no conflict occurs, just proceed with the most frequent ch i.e the one we popped earlier
            else:
                res += ch
                count += 1
        # if ch is still usable push back into the heap
            if count:
                heapq.heappush(maxHeap, [count, ch])
        
        return res