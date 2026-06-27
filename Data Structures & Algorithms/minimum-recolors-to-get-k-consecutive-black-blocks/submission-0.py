class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, 0
        n = len(blocks)

        wCount, minW = 0, float('inf')
        while r < n:
            if blocks[r] == 'W':
                wCount += 1
            if (r - l) + 1 == k:
                minW = min(minW, wCount)
                if blocks[l] == 'W':
                    wCount -= 1
                l += 1
            r += 1

        return minW