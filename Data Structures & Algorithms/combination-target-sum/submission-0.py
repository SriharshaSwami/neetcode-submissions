class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i, cur_set, cur_sum):
            if cur_sum == target:
                res.append(cur_set.copy())
                return
            
            if i >= n or cur_sum > target:
                return 

            cur_set.append(nums[i])
            dfs(i, cur_set, cur_sum + nums[i])

            cur_set.pop()
            dfs(i + 1, cur_set, cur_sum)

        dfs(0, [], 0)
        return res