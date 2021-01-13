# 207. Course Schedule
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)
        traced = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)

            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True

    def can_Finish_visited(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            # 이미 방문했던 노드이면 True
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)

            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True


class Solution2:
    def can_finish(self, numCourses, prerequisites):
        def find_parent_pc(parent, x):
            if parent[x] != x:
                return find_parent_pc(parent, parent[x])
            return parent[x]

        def union_parent(parent, a, b):
            a = find_parent_pc(parent, a)
            b = find_parent_pc(parent, b)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b

        parent_table = [0] * (numCourses + 1)
        for i in range(1, numCourses + 1):
            parent_table[i] = i

        for i in prerequisites:
            if find_parent_pc(parent_table, i[0]) == find_parent_pc(parent_table, i[1]):
                return False
            else:
                union_parent(parent_table, i[0], i[1])
        return True


sol = Solution()
sol2 = Solution2()
num_courses1, prerequisites1 = 2, [[1, 0]]
num_courses2, prerequisites2 = 2, [[1, 0], [0, 1]]
print(sol.canFinish(num_courses1, prerequisites1))
print(sol.can_Finish_visited(num_courses1, prerequisites2))
print(sol2.can_finish(num_courses1, prerequisites2))
