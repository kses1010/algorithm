# 전보
import heapq
import sys


def solution(n, c, graph):
    inf = sys.maxsize
    distance = [inf] * (n + 1)
    q = []
    heapq.heappush(q, (c, 0))
    distance[c] = 0
    while q:
        node, dist = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

    count = 0
    max_distance = 0
    print(distance)
    for i in distance:
        if i != inf:
            count += 1
            max_distance = max(max_distance, i)

    # 시작 노드는 제외해야 하므로 count - 1을 출력
    return count - 1, max_distance


n1, m1, c1 = 3, 2, 1
arr = [[],
       [(2, 4), (3, 2)],
       [],
       []]
print(solution(n1, c1, arr))
