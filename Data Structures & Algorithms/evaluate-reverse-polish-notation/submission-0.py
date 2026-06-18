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
            if i.isdigit():
                stack.append(i)
            else:
                y=int(stack.pop())
                x=int(stack.pop())
                stack.append(look_up[i](x,y))
        return stack[-1]