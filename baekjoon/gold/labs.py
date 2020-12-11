# 14502 - 연구소
import copy
from sys import stdin

inputs = stdin.readline

n, m = map(int, inputs().split())

# 연구소 지도
lab = [list(map(int, inputs().split())) for _ in range(n)]
# 안전 영역
safe_area = 0
virus = []

# 네가지 방향 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 지도
for x in range(n):
    for y in range(m):
        if lab[x][y] == 2:
            virus.append([x, y])


def bfs():
    global safe_area
    q = copy.deepcopy(virus)
    # 벽 설치 후 연구소 지도
    tmp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tmp[i][j] = lab[i][j]

    # 바이러스 살포
    while q:
        t = q.pop()
        x = t[0]
        y = t[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    q.append([nx, ny])

    # 안전 구역 크기 측정
    area = 0
    for i in tmp:
        for j in i:
            if j == 0:
                area += 1
    safe_area = max(area, safe_area)


# 벽 설치
def wall(count):
    # 벽이 3개일 때 BFS 실행(바이러스 & 안전구역 측정)
    if count == 3:
        bfs()
        return

    # 벽 설치하기
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(count + 1)
                # 확인 후 해체
                lab[i][j] = 0


wall(0)
print(safe_area)
