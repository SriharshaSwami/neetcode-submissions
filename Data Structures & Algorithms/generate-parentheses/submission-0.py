class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #3 conditions
        #If opens == closes == n STOP!
        #If opend < n add "("
        #If closes < opens add ")"
        inter=[]
        res=[]
        def backtrack(opens,closes):
            if n == opens == closes:
                res.append("".join(inter))
                return 
            elif(opens<n):
                inter.append("(")
                backtrack(opens+1,closes)
                inter.pop()
            if closes<opens:
                inter.append(")")
                backtrack(opens,closes+1)
                inter.pop()
        backtrack(0,0)
        return res
