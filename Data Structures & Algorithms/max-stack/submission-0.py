class MaxStack:

    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        val = max(x, self.maxStack[-1] if self.maxStack else x)
        self.maxStack.append(val)

    def pop(self) -> int:
        self.maxStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxStack[-1]

    def popMax(self) -> int:
        maxVal = self.peekMax()

        temp = []
        while self.top() != maxVal:
            temp.append(self.pop())
        
        self.pop()
        while temp:
            self.push(temp.pop())
        
        return maxVal


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
