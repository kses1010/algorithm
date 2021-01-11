# 232. Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:

        self.peek()
        return self.output.pop()

    # 재정렬
    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output


obj = MyQueue()
obj.push(10)
obj.push(20)
obj.push(30)
print(obj.pop())
print(obj.peek())
print(obj.empty())
