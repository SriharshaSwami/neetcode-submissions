class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]):
                continue
            left,right=i+1,len(nums)-1
            while(left<right):
                while(left<right and nums[i]+nums[left]+nums[right]<0):
                    left+=1
                while(left<right and nums[i]+nums[left]+nums[right]>0):
                    right-=1
                if(nums[i]+nums[left]+nums[right]==0):
                    result.append([nums[i],nums[left],nums[right]])
                left+=1
                while(nums[left]==nums[left-1] and left<right):
                    left+=1
        return result