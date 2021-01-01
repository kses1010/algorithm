# 상하좌우

def solution(n, arr):
    y, x = 1, 1
    for i in arr:
        if i == 'L':
            if x > 1:
                x -= 1
        elif i == 'R':
            if x < n:
                x += 1
        elif i == 'U':
            if y < 1:
                y -= 1
        elif i == 'D':
            if y < n:
                y += 1

    return y, x


def solution2(n, arr):
    y, x = 1, 1
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']
    for move in arr:
        for i in range(len(move_types)):
            if move == move_types[i]:
                ny = y + dy[i]
                nx = x + dx[i]
                if nx < 1 or ny < 1 or nx > n or ny > n:
                    continue
                y, x = ny, nx
    return y, x


n1, arr1 = 5, ['R', 'R', 'R', 'U', 'D', 'D']

print(solution(n1, arr1))
print(solution2(n1, arr1))
