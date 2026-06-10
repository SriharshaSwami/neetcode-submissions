class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxLeft=[0]*n
        maxRight=[0]*n
        res=0
        for i in range(1,len(height)):
            maxLeft[i]=max(height[i-1],maxLeft[i-1])
        for i in range(len(height)-2,-1,-1):
            maxRight[i]=max(height[i+1],maxRight[i+1])
        print(len(maxLeft),len(maxRight),n)
        for i in range(n):
            water=min(maxRight[i],maxLeft[i])-height[i]
            if water>0:
                res+=water
        return res