class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #3 conditions
        #If opens == closes == n STOP!
        #If opend < n add "("
        #If closes < opens add ")"
        inter=""
        res=[]
        def backtrack(opens,closes,inter):
            if n == opens == closes:
                res.append(inter)
                return 
            elif(opens<n):
                inter+="("
                backtrack(opens+1,closes,inter)
                inter=inter[:-1]
            if closes<opens:
                inter+=")"
                backtrack(opens,closes+1,inter)
                inter=inter[:-1]
        backtrack(0,0,inter)
        return res
