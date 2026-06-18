class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        up = 0
        for down in range(len(t)):
            if s[up] == t[down]:
                up += 1
            if up == len(s) - 1:
                return True
        return False