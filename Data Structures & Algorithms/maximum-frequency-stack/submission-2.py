class FreqStack:

    def __init__(self):
        self.stack={}
        self.maxCnt=0
        self.cnt={}

    def push(self, val: int) -> None:
        if val not in self.cnt:
            self.cnt[val]=1
        else:
            self.cnt[val]+=1
        self.maxCnt=max(self.maxCnt,self.cnt[val])
        self.stack[self.cnt[val]]=[]
        self.stack[self.cnt[val]].append(val)

    def pop(self) -> int:
        res=self.stack[self.maxCnt].pop()
        self.cnt[res]-=1
        if not self.stack[self.maxCnt]:
            self.maxCnt-=1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()