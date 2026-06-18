class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        res = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            res = min(res, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mis - 1
        return res