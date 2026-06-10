class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if len(count) < 3:
                continue
            
            newCount = defaultdict(int)
            for num, c in count.items():
                if c > 1:
                    newCount[num] = c - 1
            count = newCount
        res =[]
        for num in count:
            if nums.count(num) > n // 3:
                res.append(num)
        return res
