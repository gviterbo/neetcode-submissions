class MinStack:
    
    def __init__(self):
        self.s = []
        self.l = []
        self.m = 0

    def push(self, val: int) -> None:
        if len(self.l) == 0:
            self.m = val
        else:
            self.m = min(self.l[-1], val)
        self.s.append(val)
        self.l.append(self.m)
        
    def pop(self) -> None:
        self.s.pop()
        self.l.pop()
        if len(self.l) == 0:
            self.m = 0
        else: 
            self.m = self.l[-1]

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m
        
        