# 46. Permutations
from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = [i for i in permutations(nums)]
        return answer

    def permute_dfs(self, nums):
        results = []
        prev_element = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                # 깊은 복사 (list.copy())
                results.append(prev_element[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_element.append(e)
                dfs(next_elements)
                prev_element.pop()

        dfs(nums)
        return results


sol = Solution()
print(sol.permute([1, 2, 3]))
print(sol.permute_dfs([1, 2, 3]))
