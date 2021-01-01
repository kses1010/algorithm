# 음료수 얼려 먹기
from collections import deque


def solution(arr):
    # DFS 로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
    def dfs(x, y):
        # 주어진 범위를 벗어나는 경우에는 즉시 종료
        if x <= -1 or x >= len(arr) or y <= -1 or y >= len(arr[0]):
            return False
        # 현재 노드를 아직 방문하지 않았다면
        if arr[x][y] == 0:
            # 해당 노드 방문 처리
            arr[x][y] = 1
            # 상, 하, 좌, 우 위치도 모두 재귀적으로 호출
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
        return False

    # 모든 노드(위치)에 대하여 음료수 채우기
    result = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            # 현재 위치에서 DFS 수행
            if dfs(i, j):
                result += 1
    return result


def solution2(arr):
    n, m = len(arr), len(arr[0])
    check = [[0] * m for _ in range(n)]
    count = 0

    def bfs(a, b):
        q = deque()
        q.append((a, b))
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        check[a][b] = 1
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if not check[nx][ny] and not arr[nx][ny]:
                    q.append((nx, ny))
                    check[nx][ny] = 1

    for i in range(n):
        for j in range(m):
            if not check[i][j] and not arr[i][j]:
                bfs(i, j)
                count += 1

    return count


arr1 = [[0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]]

print(solution2(arr1))
print(solution(arr1))
