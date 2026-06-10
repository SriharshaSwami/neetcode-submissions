class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        res=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        sorted_items=sorted(d.items(),reverse=True, key=lambda x:x[1])
        print(sorted_items)
        for i in range(k):
            res.append(sorted_items[i][0])
        return res