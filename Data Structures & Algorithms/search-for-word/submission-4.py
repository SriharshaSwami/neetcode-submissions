class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        rows, cols = len(grid), len(grid[0])
        look_up = set()
        rd = [0, 0, -1, 1]
        cd = [1, -1, 0, 0]
        res = False
        def find(r, c, idx):
            nonlocal res
            if idx == len(word):
                return True
#If bounds reached or again visiting or not the req char, then return False
            if(r < 0 or c < 0 or r >= rows or c >= cols or
            (r, c) in look_up or grid[r][c] != word[idx]):
                return False
            
            look_up.add((r, c))

#Checking neighbours, if found True update res
            for i in range(len(rd)):
                if(find(r + rd[i], c + cd[i], idx + 1)):
                    res = True
#Remove the indices when backtracking
            look_up.remove((r, c))
            return res

        for i in range(rows):
            for j in range(cols):
                if find(i, j, 0):
                    return True
        return False
