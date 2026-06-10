class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        look_up={
            "+":lambda a,b:a+b,
            "-":lambda a,b:a-b,
            "*":lambda a,b:a*b,
            "/":lambda a,b:int(a/b)
        }
        for i in tokens:
            if i not in look_up:
                stack.append(int(i))
            else:
                y=stack.pop()
                x=stack.pop()
                stack.append(look_up[i](x,y))
        return stack[-1]