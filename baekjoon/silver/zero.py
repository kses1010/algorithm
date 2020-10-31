# 10773

import sys

num = int(sys.stdin.readline().rstrip())
num_list = []
for i in range(num):
    count = int(sys.stdin.readline().rstrip())
    if count != 0:
        num_list.append(count)
    else:
        if num_list:
            num_list.pop()

print(sum(num_list))