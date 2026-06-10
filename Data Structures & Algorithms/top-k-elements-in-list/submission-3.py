class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [[] for i in range(n + 1)]
        countMap = {}
        result = []
        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)
        for num in countMap:
            bucket[countMap[num]].append(num)
        print(bucket)
        for i in range(n, 0, -1):
            for j in range(len(bucket[i])):
                while bucket[i] and len(result) != k:
                    result.append(bucket[i].pop())
        return result