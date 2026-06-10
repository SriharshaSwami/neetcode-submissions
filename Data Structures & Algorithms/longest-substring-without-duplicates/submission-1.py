class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        maxLength = 0
        hashMap = set()
        left, right = 0, 0
        while right < n:
            if s[right] not in hashMap:
                hashMap.add(s[right])
                maxLength = max(maxLength, right - left + 1)
                right += 1
            else:
                while s[right] in hashMap:
                    hashMap.remove(s[left])
                    left += 1
        return maxLength

