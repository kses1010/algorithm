# 팀 결성

def solution(n, arr):
    parent_table = [0] * len(arr)
    # 부모 테이블 자기 자신 초기화
    for i in range(0, len(arr)):
        parent_table[i] = i

    def find_parent(parent, x):
        if parent[x] != x:
            return find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    answer = []
    for i in arr:
        oper, t1, t2 = i[0], i[1], i[2]
        if oper == 0:
            union_parent(parent_table, t1, t2)
        elif oper == 1:
            if find_parent(parent_table, t1) == find_parent(parent_table, t2):
                answer.append("YES")
            else:
                answer.append("NO")
    return answer


n1 = 7
arr1 = [[0, 1, 3],
        [1, 1, 7],
        [0, 7, 6],
        [1, 7, 1],
        [0, 3, 7],
        [0, 4, 2],
        [0, 1, 1],
        [1, 1, 1]]

print(solution(n1, arr1))
