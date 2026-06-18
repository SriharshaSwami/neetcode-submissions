class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
            if len(count) > 2:
                for num in count:
                    count[num] -= 1
                    if count[num] == 0:
                        del count[num]
        res = []
        for num in count:
            if count[num] > n // 3:
                res.append(num)
        return res