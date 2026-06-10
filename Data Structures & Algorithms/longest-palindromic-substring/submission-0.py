class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        palin = ""
        curLen = 0
        for i in range(n):
            #Odd lengths less goo
            left, right = i, i
            while(left >= 0 and right < n and s[left] == s[right]):
                if(curLen < (right - left + 1)):
                    palin = s[left:right + 1]
                    curLen = right - left + 1
                left -= 1
                right += 1
            #Even length less goo
            left, right = i, i + 1
            while(left >= 0 and right < n and s[left] == s[right]):
                if(curLen < (right - left + 1)):
                    palin = s[left:right + 1]
                    curLen = right - left + 1
                left -= 1
                right += 1
        return palin




"""
  l   r
a b c d
0 1 2 3


"""
            
