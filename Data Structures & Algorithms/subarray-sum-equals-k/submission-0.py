class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subArrays=[]
        counter=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                subArrays.append(sum(nums[i:j+1]))
        print(subArrays)
        for i in subArrays:
            if i==k:
                counter+=1
        return counter