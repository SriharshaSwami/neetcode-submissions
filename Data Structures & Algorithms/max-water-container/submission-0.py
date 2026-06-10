class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_Area = 0
        while left < right:
            cur_Min_Height = min(height[left], height[right])
            max_Area = max(max_Area, cur_Min_Height * (right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_Area