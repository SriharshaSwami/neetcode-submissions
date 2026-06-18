class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap={}
        for i in nums:
            if i not in hashMap:
                hashMap[i]=1
            else:
                hashMap+=1
        result=[]
        for i in hashMap:
            if(hashMap[i]>len(nums)//3):
                result.append(i)
        return result