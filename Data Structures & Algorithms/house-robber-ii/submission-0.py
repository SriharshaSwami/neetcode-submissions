class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        def robb(arr):
            n = len(arr)
            if n < 2: return arr[0]
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]
        return max(robb(nums[:N - 1]), robb(nums[1:]))
        