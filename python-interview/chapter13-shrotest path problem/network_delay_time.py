# 743. Network Delay Time
import collections
import heapq
from math import inf


class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))
        print(graph)
        # 큐 변수: [(소요 시간, 정점)]
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1

    def network_delay_time(self, times, n, k):
        graph = [[] for _ in range(n + 1)]
        # 그래프 생성
        for u, v, w in times:
            graph[u].append((v, w))

        # 거리 테이블
        dist_table = [inf] * (n + 1)
        q = []
        heapq.heappush(q, (k, 0))
        dist_table[k] = 0

        while q:
            # 가장 최단 거리가 짧은 노드 정보 꺼내기(노드, 거리)
            node, dist = heapq.heappop(q)
            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if dist_table[node] < dist:  # 노드에서 꺼낸 값이 테이블의 있는 값보다 크다면
                continue
            for i in graph[node]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 거리테이블 갱신
                if cost < dist_table[i[0]]:
                    dist_table[i[0]] = cost
                    heapq.heappush(q, (i[0], cost))
        answer = []
        for i in range(1, n + 1):
            # 도달할 수 없을 경우 -1로 추가
            if dist_table[i] == inf:
                answer.append(-1)
            else:
                answer.append(dist_table[i])

        if -1 in answer:
            return -1
        return max(answer)


sol = Solution()
times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
times2 = [[1, 2, 1], [2, 3, 2], [1, 3, 1]]

# print(sol.networkDelayTime(times1, 4, 2))
print(sol.network_delay_time(times1, 4, 2))
print(sol.network_delay_time([[1, 2, 1]], 2, 2))
print(sol.network_delay_time(times2, 3, 2))
