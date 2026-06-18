class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        countsMap = Counter(s)
        maxChar = "a"
        maxFreq = 0
        for key, val in countsMap.items():
            if maxFreq < val:
                maxFreq = val
                maxChar = key

        # early exit if solution does not exist
        if maxFreq > (n + 1) // 2:
            return ""

        res = [''] * n
        idx = 0
        # fill out even positions first 
        while countsMap[maxChar]:
            res[idx] = maxChar
            idx += 2
            countsMap[maxChar] -= 1
        
        # try filling up more even spaces if any remaining
        for ch in countsMap:
            while countsMap[ch]:
        # switch to odd indices when even goes out of bound
                if idx >= n:
                    idx = 1
                res[idx] = ch
                idx += 2
                countsMap[ch] -= 1
        
        return "".join(res)
"""

aa

a-2

possiblities:
aba (so, if maxFreq > n // 2 i.e here 2 > 1 i.e True) doesn't work
    (so, if maxFreq > (n // 2) + 1 i.e here 2 > 2 i.e False) nor returned correct!!


"axyy"

a-1,x-1,y-2
possible answers:
ayxy
yaxy
yayx
[y, "", y, ""]

"""