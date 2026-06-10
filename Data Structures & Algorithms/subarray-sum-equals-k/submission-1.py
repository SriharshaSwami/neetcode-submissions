class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap={}
        prefixMap[0]=1
        summ=0
        result=0
        for i in range(len(nums)):
            summ+=nums[i]
            if(summ-k in prefixMap):
                result+=prefixMap[summ-k]
            if summ in prefixMap:
                prefixMap[summ]+=1
            else:
                prefixMap[summ]=1
        return result