class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)

        sTot = defaultdict()
        tTos = defaultdict()
        for i in range(n):
            c1 = s[i]
            c2 = t[i]
        
            if ((c1 in sTot and sTot[c1] != c2) or (c2 in tTos and tTos[c2] != c1)):
                return False
            sTot[c1] = c2
            tTos[c2] = c1

        return True



