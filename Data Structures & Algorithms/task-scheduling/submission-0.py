class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # process the most frequent task first at each time, so that it wont cause more idle time in the future

        counts = Counter(tasks)
        maxHeap = [-t for t in counts.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0
# if there exits a task in heap or queue
        while maxHeap or queue:
            time += 1
# if we came in because of the heap, we compute a unit time to max heap element and add remaining to queue
            if maxHeap:
                rem = 1 + heapq.heappop(maxHeap)
                if rem != 0:
                    queue.append([rem, time + n])
# check everytime if the current time is allowing any task to enter heap from the waiting queue
            if queue and time == queue[0][1]:
# once the task is allowable to heap, then push to heap
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time
