# 1874
import sys

num_list = []
pm = []
count = 1
possibility = True
for i in range(int(sys.stdin.readline().rstrip())):
    num = int(sys.stdin.readline().rstrip())
    while count <= num:
        num_list.append(count)
        pm.append('+')
        count += 1
    if num_list[-1] == num:
        num_list.pop()
        pm.append('-')
    else:
        possibility = False


if not possibility:
    print('No')
else:
    for i in pm:
        print(i)
