# 18352 - 특정 거리의 도시 찾기
from collections import deque
from sys import stdin

inputs = stdin.readline

n, m, k, x = map(int, inputs().split())
data = [[] for _ in range(n + 1)]

# 도시간 거리 정보 받기
for i in range(m):
    a, b = map(int, inputs().split())
    data[a].append(b)

# 거리 표
dist = [-1] * (n + 1)
# 출발하는 도시의 거리는 0
dist[x] = 0

# bfs 문제라 deque 으로 문제풀기
q = deque([x])
while q:
    # 도착한 도시
    now = q.popleft()
    for city in data[now]:
        # 방문하지 않은 도시라면
        if dist[city] == -1:
            # 도시방문 표시하고 거리가 1이기 때문에 +1
            dist[city] = dist[now] + 1
            q.append(city)

# 최단 거리 K 도시 확인용 Check
check = False
for i, distance in enumerate(dist):
    # 거리표에서 최단 거리 K인 도시와 같다면
    if distance == k:
        print(i)
        check = True

# 최단 거리인 K인 도시가 없다면
if not check:
    print(-1)
