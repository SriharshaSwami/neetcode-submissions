class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        lefty='{[('
        righty=')]}'
        hash_Map={')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
            if char in lefty:
                stack.append(char)
            elif(char in righty):
                if stack and hash_Map[char]==stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
         
