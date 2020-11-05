# 1926
from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
cnt, area = 0, 0


def bfs(a, b):
    q = deque()
    q.append((a, b))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    size = 1
    check[a][b] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not check[nx][ny] and a[nx][ny]:
                q.append((nx, ny))
                check[nx][ny] = True
                size += 1
    return size


for i in range(n):
    for j in range(m):
        if not check[i][j] and a[i][j]:
            area = max(area, bfs(i, j))
            cnt += 1
print(cnt)
print(area)
