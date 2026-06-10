class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, n):
        #if sum -ve restart subarray from cur
            if cur_sum < 0:
                cur_sum = nums[i]
        #always check for max_sum before next iteration
            else:
                cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum