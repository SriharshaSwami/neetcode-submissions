class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashMap={}
        for i in nums:
            if i not in hashMap:
                hashMap[i]=1
        k=0
        print(hashMap)
        for i in hashMap:
            nums[k]=i
            k+=1
        print(nums)
        return len(hashMap)
