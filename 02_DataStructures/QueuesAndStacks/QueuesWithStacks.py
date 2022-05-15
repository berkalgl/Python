
class MyQueue:
    def __init__(self):
        self.first = []
        self.last = []

    def push(self, x: int) -> None:
        length = len(self.first)
        for i in range(0, length):
            self.last.append(self.first.pop())
        self.last.append(x)
        return self

    def pop(self) -> int:
        length = len(self.last)
        for i in range(0, length):
            self.first.append(self.last.pop())
        self.first.pop()
        return self

    def peek(self) -> int:
        if len(self.last) > 0:
            return self.last[0]
        return self.first[len(self.first)-1]

    def empty(self) -> bool:
        if(len(self.first) == 0 and len(self.last) == 0):
            return True
        return False
        


obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()