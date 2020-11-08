# 6198

import sys

count = int(sys.stdin.readline().rstrip())

buildings = []
answers = [0] * count
stack = []
for i in range(count):
    h = int(sys.stdin.readline().rstrip())
    buildings.append(h)

buildings.append(sys.maxsize)
for i, cur in enumerate(buildings):
    while stack and cur >= buildings[stack[-1]]:
        last = stack.pop()
        answers[last] = i - last - 1
    stack.append(i)

print(sum(answers))
