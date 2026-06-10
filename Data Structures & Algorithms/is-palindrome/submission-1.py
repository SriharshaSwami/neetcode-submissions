class Solution:
    def isPalindrome(self, s: str) -> bool:
        start,end=0,len(s)-1
        s=s.lower()
        print(s)
        while(start<end):
            if(not s[end].isalnum()):
                end-=1
                print(s[end])
                continue
            if(not s[start].isalnum()):
                start+=1
                print(s[start])
                continue
            if(s[start]==s[end]):
                start+=1
                end-=1
            else:return False
        return True