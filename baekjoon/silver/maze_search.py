# 2178 - 미로 탐색
from collections import deque
from sys import stdin

inputs = stdin.readline

n, m = map(int, inputs().split())
graph = [list(map(int, inputs().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

print(graph[n - 1][m - 1])
