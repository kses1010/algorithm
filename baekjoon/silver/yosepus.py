# 1158

import sys


n, k = map(int, sys.stdin.readline().rstrip().split())

arr = []
answer = []
for i in range(n):
    arr.append(i + 1)

num = 0
for i in range(n):
    num += k - 1
    if num >= len(arr):
        num = num % len(arr)
    answer.append(str(arr.pop(num)))

print("<",", ".join(answer)[:],">", sep='')
