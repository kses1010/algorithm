# 다익스트라 알고리즘

# 간단 다익스트라 알고리즘 소스코드
import heapq
import sys


def solution(n, m, start):
    INF = int(1e9)
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
    graph = [[] for i in range(n + 1)]
    # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
    vis = [False] * (n + 1)
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)
    answer = []

    # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
    def get_smallest_node():
        min_value = INF
        # 가장 최단 거리가 짧은 노드(인덱스)
        index = 0
        for i in range(1, n + 1):
            if distance[i] < min_value and not vis[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        # 시작 노드에 대해서 초기화
        distance[start] = 0
        vis[start] = True
        # 당장 start 노드와 연결이 가능한 노드의 거리를 갱신
        for i in graph[start]:
            distance[i[0]] = i[1]
        # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
        for i in range(n - 1):
            # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
            now = get_smallest_node()
            vis[now] = True
            # 현재 노드와 연결된 다른 노드를 확인
            for j in graph[now]:
                cost = distance[now] + j[i]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

    for i in range(1, n + 1):
        # 도달할 수 없다면, 무한(INFINITY)라고 출력
        if distance[i] == INF:
            answer.append('INFINITY')
        else:
            answer.append(distance[i])


def heap_dijkstra(n, start, graph):
    # 최단 거리테이블을 모두 무한으로 초기화
    inf = sys.maxsize
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [inf] * (n + 1)
    answer = []
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    # 큐가 비어있지 않다면
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        now_node, dist = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now_node] < dist:  # 노드에서 꺼낸 값이 테이블의 있는 값보다 크다면 처리된 것으로 처리(무시)
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now_node]:
            cost = dist + i[1]  # i[1]은 노드의 거리값을 의미
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 거리테이블 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

    # 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(1, n + 1):
        # 도달할 수 없는 경우, 무한으로 출력
        if distance[i] == inf:
            answer.append(False)
        else:
            answer.append(distance[i])

    return answer


n1, m1, start1 = 6, 11, 1
array = [[],
         [(2, 2), (3, 5), (4, 1)],
         [(3, 3), (4, 2)],
         [(3, 3), (6, 5)],
         [(3, 3), (5, 1)],
         [(3, 1), (6, 2)],
         []]
# print(solution(n1, m1, start1))
print(heap_dijkstra(n1, start1, array))
# [0, 2, 3, 1, 2, 4]
