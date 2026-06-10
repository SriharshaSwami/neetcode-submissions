class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output=[]
        product=1
        ZeroCount=0
        for i in range(n):
            if nums[i]==0:
                ZeroCount+=1
            else:
                product*=nums[i]
        if ZeroCount>1:
            return [0]*n
        if ZeroCount==1:
            for j in nums:
                if j!=0:
                    output.append(0)
                else:
                    output.append(product)
        if ZeroCount==0:
            for k in nums:
                output.append(int(product/k))
        return output