class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {}
        s2Count = {}
        for i in range(len(s1)):
            s1Count[s1[i]] = 1 + s1Count.get(s1[i], 0)
            s2Count[s2[i]] = 1 + s2Count.get(s2[i], 0)

        matches = 0
        for char in s1Count:
            if s1Count[char] == s2Count.get(char, 0):
                matches += 1
        if matches == len(s1Count):
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            inChar, outChar = s2[right], s2[left]
            s2Count[inChar] = 1 + s2Count.get(inChar, 0)
            if inChar in s1Count:
                #if previously not matched but after adding from right, matched
                if s1Count[inChar] == s2Count[inChar]:
                    matches += 1
                #if previously matches but after adding from right, not matched
                elif s1Count[inChar] == s2Count[inChar] - 1:
                    matches -= 1

            s2Count[outChar] -= 1
            if outChar in s1Count:
                #if previously not matched but after removing from left, matched
                if s1Count[outChar] == s2Count[outChar]:
                    matches += 1
                #if previously matches but after removing from left, not matched
                elif s1Count[outChar] == s2Count[outChar] + 1:
                    matches -= 1

            left += 1
            if matches == len(s1Count):
                    return True
        return False