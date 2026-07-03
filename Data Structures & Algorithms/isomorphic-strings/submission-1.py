class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        # create 2 hash maps for both the strings
        sTot = defaultdict()
        tTos = defaultdict()
        for i in range(n):
        # both are same length, so we can traverse simlutaneously
            c1 = s[i]
            c2 = t[i]
        # check if the char c1 is already in the map, if yes then check if it's already mapped to any other char
            if ((c1 in sTot and sTot[c1] != c2) or (c2 in tTos and tTos[c2] != c1)):
                return False
        # if no, now create the map between those new chars
            sTot[c1] = c2
            tTos[c2] = c1

        return True



