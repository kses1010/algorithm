from collections import deque


def topology_sort(graph):
    # 노드의 개수
    v = len(graph)
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (v + 1)
    # 진입차수 설정
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            indegree[graph[i][j]] += 1

    # 위상 정렬 시작

    # 알고리즘 수행 결과를 담을 리스트
    result = []
    # 큐 기능을 위한 deque 라이브러리
    q = deque()

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        node = q.popleft()
        result.append(node)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[node]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    return result


v1, e = 7, 8
graph1 = [[],
          [2, 5],
          [3, 6],
          [4],
          [7],
          [6],
          [4],
          []]
print(topology_sort(graph1))
