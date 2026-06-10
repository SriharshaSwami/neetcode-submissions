class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            if char!="]":
                stack.append(char)
                continue
            inter=""
            while(stack[-1]!="["):
                inter = stack.pop() + inter
            stack.pop()
            k=""
            while(stack and stack[-1].isdigit()):
                k = stack.pop() + k
            stack.append(int(k) * inter)
        return "".join(stack)
            
