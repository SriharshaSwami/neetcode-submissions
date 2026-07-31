class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest, m):
            curSum = 0
            subArr = 0
            for i in range(n):
                curSum += nums[i]
    # go until the currSubArr exceeds limit
                if curSum > largest:
    # if reached, consider new subArr from that element
                    curSum = nums[i]
                    subArr += 1
    # finally if count(subarr) is <= we return True else False
    # <= works because, from a subArr of k elements, ofc we can achieve k subArrays easily
            return subArr + 1 <= m


        n = len(nums)
    # that subArr sum must range minimum of max(nums) and highest it could be sum(nums)
        l, r = max(nums), sum(nums)

        while(l <= r):
            mid = (l + r) // 2

            if canSplit(mid, k):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

