# 커리큘럼
import copy
from collections import deque


def solution(arr):
    answer = []
    v = len(arr)
    indegree = [0] * (v + 1)
    # 각 강의 시간을 0으로 초기화
    time = [0] * (v + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
    graph = [[] for _ in range(v + 1)]

    # 방향 그래프의 모든 간선 정보 받기
    for i in range(1, v + 1):
        # 첫 번째 수는 시간 정보
        time[i] = arr[i - 1][0]
        for j in arr[i - 1][1:-1]:
            indegree[i] += 1
            graph[j].append(i)
    print(graph)
    # 알고리즘 수행 결과를 담을 리스트
    result = copy.deepcopy(time)
    q = deque()
    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        node = q.popleft()
        for i in graph[node]:
            result[i] = max(result[i], result[node] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    for i in range(1, v + 1):
        answer.append(result[i])

    return answer


arr1 = [[10, -1],
        [10, 1, -1],
        [4, 1, -1],
        [4, 3, 1, -1],
        [3, 3, -1]]
print(solution(arr1))
