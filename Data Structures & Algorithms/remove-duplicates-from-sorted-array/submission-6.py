class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashMap={}
        for i in nums:
            if i not in hashMap:
                hashMap[i]=1
        k=0
        for i in hashMap:
            nums[k]=i
            k+=1
        l=len(hashMap.values())
        nums=nums[:k]
        print(nums)
        return len(k)
