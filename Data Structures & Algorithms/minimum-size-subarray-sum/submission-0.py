class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        left = total = 0
        res = len(nums)

        for right in range(len(nums)):
            if total < target:
                total += nums[right]
            else:
                while(total >= target):
                    res = min(res, (right - left))    
                    total -= nums[left]
                    left += 1
        return res  