# 특정 원소가 속한 집합을 찾기
def find_parent_pc(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent_pc(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent_pc(parent, a)
    b = find_parent_pc(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선의 개수
v, e = 3, 3
# 부모 테이블 초기화
parent1 = [0] * (v + 1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent1[i] = i

list1 = [[1, 2],
         [1, 3],
         [2, 3]]

# 사이클 발생 여부
cycle = False

for i in list1:
    if find_parent_pc(parent1, i[0]) == find_parent_pc(parent1, i[1]):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(union) 수행
    else:
        union_parent(parent1, i[0], i[1])

if cycle:
    print("사이클")
else:
    print("사이클 발생하지 않음")
