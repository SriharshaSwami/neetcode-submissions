class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashMap={}
        for i in nums:
            if i not in hashMap:
                hashMap[i]=1
        for i in range(1,len(nums)+2):
            if i not in hashMap:
                return i