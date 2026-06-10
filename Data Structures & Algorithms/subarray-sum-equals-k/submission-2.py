class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = {}
        prefixSum[0] = 1
        count = total = 0
        for right in range(n):
            total += nums[right]
            if total - k in prefixSum:
                count += prefixSum[total - k]
            prefixSum[total] = 1 + prefixSum.get(total, 0)
        return count