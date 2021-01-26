# 310. Minimum Height Trees
from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # 양방향 그래프
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을때까지 반복제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                node = graph[leaf].pop()
                graph[node].remove(leaf)

                if len(graph[node]) == 1:
                    new_leaves.append(node)
            leaves = new_leaves

        return leaves


sol = Solution()
n1, edges1 = 4, [[1, 0], [1, 2], [1, 3]]
n2, edges2 = 6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
n3, edges3 = 10, [[1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [6, 10], [5, 7], [5, 8], [8, 9]]
print(sol.findMinHeightTrees(n1, edges1))
print(sol.findMinHeightTrees(n2, edges2))
print(sol.findMinHeightTrees(n3, edges3))
