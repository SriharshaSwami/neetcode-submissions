class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        while top <= bot:
            mid_Row = (top + bot)//2
            if target > matrix[mid_Row][-1]:
                top = mid_Row + 1
            elif target < matrix[mid_Row][0]:
                bot = mid_Row - 1
            else:
                break
        if top > bot:
            return False

        nums = matrix[mid_Row]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False