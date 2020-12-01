# 2493 탑
from sys import stdin

inputs = stdin.readline

n = int(inputs())

answers = [0] * n
towers = list(map(int, inputs().split()))
stack = []

for i, cur in enumerate(towers):
    while stack and cur > towers[stack[-1]]:
        stack.pop()
    if stack:
        answers[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(list(map(str, answers))))
