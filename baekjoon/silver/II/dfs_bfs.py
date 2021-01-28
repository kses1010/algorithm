# 1260 - DFS와 BFS
from collections import deque

n, m, start = map(int, input().split())

maps = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)

for node in maps:
    node.sort()
visited1 = []


def dfs(v, visited):
    visited.append(v)
    for i in maps[v]:
        if i not in visited:
            visited = dfs(i, visited)
    return visited


def bfs(start_v):
    visited = [start_v]
    q = deque([start_v])

    while q:
        v = q.popleft()
        for i in maps[v]:
            if i not in visited:
                visited.append(i)
                q.append(i)
    return visited


dfs_answer = dfs(start, visited1)
for node in dfs_answer:
    print(node, end=' ')
print()
bfs_answer = bfs(start)
for node in bfs_answer:
    print(node, end=' ')
