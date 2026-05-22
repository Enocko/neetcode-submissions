class MyQueue:

    def __init__(self):
        self.Queue = deque()

    def push(self, x: int) -> None:
        self.Queue.append(x)

    def pop(self) -> int:
        return self.Queue.popleft()

    def peek(self) -> int:
        return self.Queue[0]

    def empty(self) -> bool:
        return len(self.Queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()