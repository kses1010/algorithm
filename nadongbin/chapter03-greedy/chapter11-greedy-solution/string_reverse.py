# 1439 - 문자열 뒤집기
from sys import stdin

inputs = stdin.readline

strs = inputs().rstrip()
a, b = 0, 0

if strs[0] == '1':
    a += 1
else:
    b += 1

for i in range(len(strs) - 1):
    if strs[i + 1] != strs[i]:
        if strs[i + 1] == '1':
            a += 1
        else:
            b += 1
print(min(a, b))
