# 1647 - 도시 분할 계획
from sys import stdin

inputs = stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, e1, e2):
    e1 = find_parent(parent, e1)
    e2 = find_parent(parent, e2)
    if e1 < e2:
        parent[e2] = e1
    else:
        parent[e1] = e2


n, m = map(int, inputs().split())
parent_table = [0] * (n + 1)
edge_table = []
result = 0
for i in range(1, n + 1):
    parent_table[i] = i

for _ in range(m):
    a, b, c = map(int, inputs().split())
    edge_table.append((c, a, b))

edge_table.sort()
last = 0

for edge in edge_table:
    cost, h1, h2 = edge
    if find_parent(parent_table, h1) != find_parent(parent_table, h2):
        union_parent(parent_table, h1, h2)
        result += cost
        last = cost

print(result - last)
