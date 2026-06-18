class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        m, n = len(s1), len(s2)
        left, right = 0, len(s1)
        while right < n:
            if sorted(s1) == sorted(s2[left:right]):
                return True
            left +=1
            right +=1
        return False