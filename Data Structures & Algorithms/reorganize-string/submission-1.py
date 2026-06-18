class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        maxFreq = 0
        maxChar = ""

        for ch, val in counts.items():
            if val > maxFreq:
                maxFreq = val
                maxChar = ch
        
        if maxFreq > (n + 1) // 2:
            return ""

        idx = 0
        res = [""] * n

        while maxFreq:
            res[idx] = maxChar
            maxFreq -= 1
            idx += 2
        
        counts[maxChar] = 0

        
        for ch in counts:
            while counts[ch]:
                if idx >= n:
                    idx = 1
                res[idx] = ch
                counts[ch] -= 1
                idx += 2

        
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