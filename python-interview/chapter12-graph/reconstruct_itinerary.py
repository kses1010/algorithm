# 332. Reconstruct Itinerary
import collections
from collections import deque
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(deque)
        # 그래프 순서대로 구성
        for depart, arrive in sorted(tickets):
            graph[depart].append(arrive)
        route = []

        def dfs(start):
            # 첫 번째 값을 읽어 어휘 순으로 방문
            while graph[start]:
                dfs(graph[start].popleft())
            route.append(start)

        dfs('JFK')
        return route[::-1]

    def find_itinerary_while(self, tickets):
        graph = collections.defaultdict(deque)
        # 그래프 순서대로 구성
        for depart, arrive in sorted(tickets):
            graph[depart].append(arrive)

        route, stack = [], ["JFK"]
        while stack:
            # 반복으로 스택을 구성하지만 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].popleft())
            route.append(stack.pop())

        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]


tickets1 = [["MUC", "LHR"],
            ["JFK", "MUC"],
            ["SFO", "SJC"],
            ["LHR", "SFO"]]
sol = Solution()
print(sol.findItinerary(tickets1))
print(sol.find_itinerary_while(tickets1))
