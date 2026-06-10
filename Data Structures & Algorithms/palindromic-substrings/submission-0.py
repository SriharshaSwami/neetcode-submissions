class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            #Odd len
            left, right = i, i
            while left > -1 and right < n and s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
            
            #Even len
            left, right = i, i + 1
            while left > -1 and right < n and s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
        return count



"""

a b a a
0 1 2 3

count = 4
"""