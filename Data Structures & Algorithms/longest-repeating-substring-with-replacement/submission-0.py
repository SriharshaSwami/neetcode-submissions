class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        hashMap = {}
        left = res = maxf = 0
        for right in range(n):
            hashMap[s[right]] = 1 + hashMap.get(s[right], 0)
            maxf = max(maxf, hashMap[s[right]])
            while(right - left + 1) - maxf > k:
                hashMap[s[left]] -= 1
                left += 1
            res = max(res, (right - left) + 1)
        return res
            