class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest, m):
            curSum = 0
            subArr = 0
            for i in range(n):
                curSum += nums[i]
                if curSum > largest:
                    curSum = nums[i]
                    subArr += 1
            return subArr + 1 <= m


        n = len(nums)
        l, r = max(nums), sum(nums)

        while(l <= r):
            mid = (l + r) // 2

            if canSplit(mid, k):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

