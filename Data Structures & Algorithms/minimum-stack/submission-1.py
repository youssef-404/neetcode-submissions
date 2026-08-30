class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val,self.minStack[-1]))    
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
