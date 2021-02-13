class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = [sys.maxsize]



    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minStack.append(min(self.minStack[-1], x))



    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()