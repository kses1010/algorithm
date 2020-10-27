# 1406

# 시간 초과로 실패
import sys

word = list(str(input()))
count = int(input())
cursor = len(word) - 1
for i in range(count):
    commend = input().split()

    if commend == 'L' and cursor != 0:
        cursor -= 1
    elif commend == 'D' and cursor != len(word) - 1:
        cursor += 1
    elif commend == 'B' and cursor != 0:
        del word[cursor - 1]
    elif commend[0] == 'P':
        input_word = commend[1]
        word.insert(cursor + 1, input_word)

print(''.join(word))


strings = sys.stdin.readline().rstrip()
cmds = int(sys.stdin.readline().rstrip())
left = []
right = []

for i in range(len(strings)):
    left.append(strings[i])

for i in range(cmds):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'L':
        if len(left):
            move = left.pop()
            right.append(move)
    elif cmd[0] == 'D':
        if len(right):
            move = right.pop()
            left.append(move)
    elif cmd[0] == 'P':
        left.append(cmd[1])
    else:
        if len(left):
            left.pop()

print(''.join(left + right[::-1]))
