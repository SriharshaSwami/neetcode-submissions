class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        n=len(operations)
        for i in range(n):
            if(operations[i] =='+'):
                x=res[-1]+res[-2]
                res.append(x)
            elif(operations[i]=='D'):
                res.append(res[-1]*2)
            elif(operations[i]=='C'):
                res.pop()
            else:
                res.append(int(operations[i]))
            print(res)
        return sum(res)