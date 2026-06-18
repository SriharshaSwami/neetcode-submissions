class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if(nums[i]+nums[j]+nums[k]==0):
                        result.append([nums[i],nums[j],nums[k]])
        return result