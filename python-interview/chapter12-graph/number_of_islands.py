# 200. Number of Islands


from collections import deque


class Solution:
    def dfs(self, grid, i, j):
        # 더 이상 땅이 아닌 경우 종료
        if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
            return

        grid[i][j] = '0'
        # 동서남북 탐색
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    def numIslands(self, grid: [[str]]) -> int:
        # 예외처리
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    # 모든 육지 탐색후 카운트 1 증가
                    count += 1
        return count


class Solution2:
    def num_is_lands(self, grid: [[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(x, y):
            # 좌표가 섬 그래프에서 벗어나거나 물(0)일 경우 탈출
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == '0':
                return

            grid[x][y] = '0'

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


# bfs 로 문제 해결
class Solution3:
    def num_is_land_bfs(self, grid):
        n, m = len(grid), len(grid[0])
        # 방문 리스트
        check = [[0] * m for _ in range(n)]
        count = 0

        def bfs(a, b):
            # 좌표 방향
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            q = deque()
            q.append((a, b))
            # 방문표시
            check[a][b] = 1

            while q:
                x, y = q.popleft()
                # 상하좌우 방향 확인
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]

                    # 좌표가 그래프 밖으로 벗어날 때
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    # 체크리스트에는 방문하지 않았으나 맵에선 육지(1)일 경우
                    if not check[nx][ny] and grid[nx][ny] == "1":
                        # 체크리스트에 추가하고
                        check[nx][ny] = 1
                        # 큐에 추가
                        q.append((nx, ny))

        for i in range(n):
            for j in range(m):
                if not check[i][j] and grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        return count


sol = Solution()
sol2 = Solution2()
sol3 = Solution3()
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

# print(sol.numIslands(grid1))
print(sol3.num_is_land_bfs(grid1))
print(sol3.num_is_land_bfs(grid2))
print(sol2.num_is_lands(grid1))
# print(sol.numIslands(grid2))
print(sol2.num_is_lands(grid2))
