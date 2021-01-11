# 225. Implement Stack using Queues

import collections


class MyStack:
    def __init__(self):
        self.q = collections.deque()

    # 삽입 후 재정렬
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


obj = MyStack()
obj.push(10)
obj.push(20)
print(obj.pop())
print(obj.top())
print(obj.empty())
