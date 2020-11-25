# 왕실의 나이트

def solution(s):
    y, x = int(ord(s[0])) - int(ord('a')) + 1, int(s[1])
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]
    count = 0
    for step in steps:
        next_y = y + step[0]
        next_x = x + step[1]
        if 1 <= next_x <= 8 and 1 <= next_y <= 8:
            count += 1
    return count


print(solution('a1'))
