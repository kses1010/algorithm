# 56. Merge Intervals
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort(key=lambda x: x[0])

        for i in intervals:
            if answer and i[0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], i[1])
            else:
                answer += [i]
        return answer


sol = Solution()
intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals2 = [[1, 4], [4, 5]]
print(sol.merge(intervals1))
print(sol.merge(intervals2))
