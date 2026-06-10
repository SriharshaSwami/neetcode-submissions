class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=i
        for i in range(len(nums)):
            if(target-nums[i] in d and i!=d[target-nums[i]]):
                return sorted([i,d[target-nums[i]]])
        
        
