class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        while(left<right):
            if(s[left]!=s[right]):
                skipLeft,skipRight=s[left+1:right+1],s[left:right]
                if(skipLeft==skipLeft[::-1] or skipRight==skipRight[::-1]):
                    return True
                else:return False
            left+=1
            right-=1
        return True