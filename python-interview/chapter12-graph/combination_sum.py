# 39. Combination Sum
from itertools import combinations
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                answer.append(path)
                return

            # 자신부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return answer

    def combination_sum(self, candidates, target):
        answer = []

        def dfs(index, num_list):
            if sum(num_list) > target:
                return
            if sum(num_list) == target:
                answer.append(num_list)
                return

            for i in range(index, len(candidates)):
                dfs(i, num_list + [candidates[i]])

        dfs(0, [])
        return answer


sol = Solution()
candi1, target1 = [2, 3, 6, 7], 7
candi2, target2 = [2, 3, 5], 8
# print(sol.combinationSum(candi1, target1))
print(sol.combination_sum(candi1, target1))
# print(sol.combinationSum(candi2, target2))
