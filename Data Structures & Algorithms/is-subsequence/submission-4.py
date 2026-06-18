class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        up = 0
        if s == "": return True
        for down in range(len(t)):
            if s[up] == t[down]: up += 1

        return up == len(s)