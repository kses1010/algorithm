# 787. Cheapest Flights Within K Stops
import collections
import heapq
from math import inf
from typing import List


class Solution:
    # 기존의 테이블을 이용한 다익스트라 알고리즘 -> 3번째 테스트에서 통과하지 않음.
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int):
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        distance = [inf] * n
        q = []
        heapq.heappush(q, (0, src, K))
        distance[src] = 0

        while q:
            price, node, K = heapq.heappop(q)
            if K >= 0:
                if distance[node] < price:
                    continue
                for v, w in graph[node]:
                    cost = price + w
                    if cost < distance[v]:
                        distance[v] = cost
                        heapq.heappush(q, (cost, v, K - 1))

        return distance

    # 파이썬 알고리즘 인터뷰 책 코드
    def find_cheapest_price(self, n, flights, src, dst, K):
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        q = [(0, src, K)]

        while q:
            price, node, K = heapq.heappop(q)
            if node == dst:
                return price
            if K >= 0:
                for v, w in graph[node]:
                    cost = price + w
                    heapq.heappush(q, (cost, v, K - 1))

        return -1


edges1 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
edges2 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
edges3 = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
sol = Solution()
print(sol.findCheapestPrice(3, edges1, 0, 2, 1))
print(sol.findCheapestPrice(3, edges1, 0, 2, 0))
print(sol.findCheapestPrice(5, edges3, 0, 2, 2))
print(sol.find_cheapest_price(5, edges3, 0, 2, 2))
