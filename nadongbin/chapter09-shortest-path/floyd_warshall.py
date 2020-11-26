# 플로이드 워셜 알고리즘
import sys


def floyd_warshall(arr, n):
    inf = sys.maxsize
    # 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
    graph = [[inf] * (n + 1) for _ in range(n + 1)]
    answer = []
    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행 K는 거처가는 노드. A는 출발, B는 도착 노드
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 수행된 결과를 출력
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # 도달할 수 없는 경우, 무한으로 출력
            if graph[a][b] == inf:
                answer.append("무한")
            # 도달할 수 있는 경우 거리를 출력
            else:
                answer.append(graph[a][b])
    return answer
