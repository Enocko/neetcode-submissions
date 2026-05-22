class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        n = 1
        while self.stack and self.stack[-1][1] <= price:
            n += self.stack.pop()[0]

        self.stack.append([n, price])
        return n

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)