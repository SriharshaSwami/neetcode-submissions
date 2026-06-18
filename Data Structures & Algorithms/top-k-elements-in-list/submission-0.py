class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        res=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if(d[i]>=k):
                res.append(i)
        return res

        
            