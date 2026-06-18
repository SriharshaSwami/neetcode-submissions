class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft=[]
        maxRight=[]
        lefty=0
        righty=0
        res=0
        for i in range(1,len(height)):
            maxLeft.append(lefty)
            lefty=max(height[i-1],lefty)
        for i in range(len(height)-2,-1,-1):
            maxRight.append(righty)
            righty=max(height[i+1],righty)
        maxRight.reverse()
        for i in range(1,len(height)-1):
            water=min(maxRight[i],maxLeft[i])-height[i]
            if(water>0):
                res+=water
        return res