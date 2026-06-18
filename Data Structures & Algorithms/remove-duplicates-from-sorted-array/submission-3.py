class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashMap={}
        for i in nums:
            if i not in hashMap:
                hashMap[i]=1
        k=0
        for i in hashMap:
            nums[k]=i
        l=len(hashMap.values())
        nums=nums[:k+1]
