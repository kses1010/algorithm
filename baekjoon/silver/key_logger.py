# 5397

import sys
from collections import deque

test_count = int(sys.stdin.readline())

for i in range(test_count):
    word = []
    left, right = deque(), []
    password = list(sys.stdin.readline().rstrip())
    for k in password:
        if k.isalnum():
            left.append(k)

    for j in range(len(password)):
        if password[j] == '-':
            if len(word):
                word.pop()
        elif password[j] == '<':
            if len(word):
                temp = word.pop()
                right.append(temp)
        elif password[j] == '>':
            if len(right):
                temp = right.pop()
                word.append(temp)
        else:
            temp = left.popleft()
            word.append(temp)

    print(''.join(word + right[::-1]))
