class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i] = [tasks[i][0], i, tasks[i][1]]
        tasks.sort()

        for t in tasks:
            t[0], t[2] = t[2], t[0]

        sortedTasks = deque(tasks)
        print(sortedTasks)

        minHeap = []
        heapq.heapify(minHeap)
        res = []

        time = sortedTasks[0][2]
        while(1):
            while(sortedTasks and time >= sortedTasks[0][2]):
                newTask = sortedTasks.popleft()
                heapq.heappush(minHeap, [newTask[0], newTask[1]])
            if minHeap:
                [pTime, idx] = heapq.heappop(minHeap)
                time += pTime
                res.append(idx)
            else:
                if sortedTasks:
                    time = sortedTasks[0][2]
            if not sortedTasks and not minHeap:
                break

        return res