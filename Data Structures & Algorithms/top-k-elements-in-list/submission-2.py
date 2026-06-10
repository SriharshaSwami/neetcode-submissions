class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        freq=[[] for i in range(len(nums)+1)]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for num,count in d.items():
            freq[count].append(num)
        res=[]
        print(freq)
        for i in range(len(nums),0,-1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if(len(res)==k):
                    return res
