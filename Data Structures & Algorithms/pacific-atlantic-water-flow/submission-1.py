class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        ncols = [1, -1, 0, 0]
        nrows = [0, 0, -1, 1]
        pacific, atlantic = set(), set()
        def dfs(r, c, ocean, prev_height):
            if(((r, c) in ocean) or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prev_height):
                return 
            ocean.add((r, c))
            # for i in range(len(ncols)):
            #     nr = r + nrows[i]
            #     nc = c + ncols[i]
            #     if 0 <= nr < rows and 0 <= nc < cols:
            #         dfs(nr, nc, ocean, heights[nr][nc])
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])


        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        return [list(cell) for cell in pacific.intersection(atlantic)]


