class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(0,len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            left,right=i+1,len(nums)-1
            while(left<right):
                if(nums[i]+nums[left]+nums[right]<0):
                    left+=1
                elif(nums[i]+nums[left]+nums[right]>0):
                    right-=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    curLeft=nums[left]
                    left+=1
                    curRight=nums[right]
                    right-=1
                    while(left<right and nums[left]==curLeft):
                        left+=1
                    while(left<right and nums[right]==curRight):
                        right-=1
        return result