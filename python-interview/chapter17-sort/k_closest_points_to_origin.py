# 973. K Closest Points to Origin
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int):
        point_dist_list = []
        for x, y in points:
            dist = (x ** 2 + y ** 2) ** 0.5
            point_dist_list.append((x, y, dist))
        point_dist_list.sort(key=lambda a: a[2])
        answers = [[i[0], i[1]] for i in point_dist_list]
        return answers[:K]

    def k_closest(self, points, k):
        heap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        answers = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            answers.append((x, y))
        return answers

sol = Solution()
points1, k1 = [[1, 3], [-2, 2]], 1
points2, k2 = [[3, 3], [5, -1], [-2, 4]], 2
print(sol.kClosest(points1, k1))
print(sol.kClosest(points2, k2))
print(sol.k_closest(points1, k1))
print(sol.k_closest(points2, k2))
