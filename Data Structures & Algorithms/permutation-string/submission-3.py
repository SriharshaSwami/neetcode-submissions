class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Map = {}
        s2Map = {}
        matches = 0

        for char in range(len(s1)):
            s1Map[s1[char]] = 1 + s1Map.get(s1[char], 0)
            s2Map[s2[char]] = 1 + s2Map.get(s2[char], 0)
        for key in s1Map:
            if s1Map[key] == s2Map.get(key, 0):
                matches += 1
        
        if matches == len(s1Map):
                return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            s2Map[s2[right]] = 1 + s2Map.get(s2[right], 0)
            if s1Map.get(s2[right], 0) == s2Map[s2[right]]:
                matches += 1
            elif s2Map[s2[right]] - 1 == s1Map.get(s2[right], 0):
                matches -= 1

            s2Map[s2[left]] -= 1
            if s1Map.get(s2[left], 0) == s2Map[s2[left]]:
                matches += 1
            elif s2Map[s2[left]] + 1 == s1Map.get(s2[left], 0):
                matches -= 1
            left += 1
            if matches == len(s1Map):
                return True
        return False