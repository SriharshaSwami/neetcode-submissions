class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if(i not in d):
                d[i]=1
            else:
                d[i]+=1
        for j in d:
            if d[j]>1:
                return True
        return False