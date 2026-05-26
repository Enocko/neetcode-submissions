class FreqStack:

    def __init__(self):
        self.h = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.h[val] += 1
        self.stack.append(val)

    def pop(self) -> int:
        maxCnt = max(self.h.values())
        i = len(self.stack)-1
        while self.h[self.stack[i]] != maxCnt:
            i -= 1
        
        self.h[self.stack[i]] -= 1
        return self.stack.pop(i)


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


"""
self.h = {
    5: 3,
    7: 2,
    4: 1
}

self.stack = [5, 7, 5, 7, 4, 5]
maxCnt = 3




stack = {1: [5, 7, 4]
         2: [5, 7]
         3: [5]
}
"""