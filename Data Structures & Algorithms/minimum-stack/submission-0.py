class MinStack:

    def __init__(self):
        self.s1=[]
        self.Min=[]
    def push(self, val: int) -> None:
        self.s1.append(val)
        if not self.Min:
            self.Min.append(val)
        else:
            self.Min.append(min(self.Min[-1],val))

    def pop(self) -> None:
        self.Min.pop()
        self.s1.pop()

    def top(self) -> int:
        return self.s1[len(self.s1)-1]

    def getMin(self) -> int:
        return self.Min[-1]
