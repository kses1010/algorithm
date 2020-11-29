def find_parent_node(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent_node(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent_node(parent, a)
    b = find_parent_node(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, edge = 7, 9
parent_table = [0] * (v + 1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent_table[i] = i

list1 = [[1, 2, 29],
         [1, 5, 75],
         [2, 3, 35],
         [2, 6, 34],
         [3, 4, 7],
         [4, 6, 23],
         [4, 7, 13],
         [5, 6, 53],
         [6, 7, 25]]

# 비용순으로 정렬하기 위한 튜플의 첫 번째 원소를 비용으로 설정
for i in list1:
    edges.append((i[2], i[0], i[1]))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하기
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent_node(parent_table, a) != find_parent_node(parent_table, b):
        union_parent(parent_table, a, b)
        result += cost

print(result)
