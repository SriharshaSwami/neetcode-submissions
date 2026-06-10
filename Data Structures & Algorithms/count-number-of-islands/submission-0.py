class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def find(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return 0
            
            grid[r][c] = "0"

            find(r + 1, c)
            find(r - 1, c)
            find(r, c + 1)
            find(r, c - 1)
            
            return 1

        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    count += find(i, j)
        return count
