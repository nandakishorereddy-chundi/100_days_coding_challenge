class MyQueue:

    def __init__(self):
        self.q = []
        self.ix = 0

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        elem = self.q[self.ix]
        self.ix += 1
        return elem

    def peek(self) -> int:
        return self.q[self.ix]

    def empty(self) -> bool:
        return self.ix == len(self.q)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()