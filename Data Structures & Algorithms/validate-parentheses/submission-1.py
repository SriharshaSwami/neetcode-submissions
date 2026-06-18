class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        lefty='{[('
        righty=')]}'
        hash_Map={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if i in lefty:
                stack.append(i)
            elif(i in righty):
                if stack and hash_Map[i]==stack[-1]:
                    stack.pop()
                    continue
                else:return False
        return True
         
