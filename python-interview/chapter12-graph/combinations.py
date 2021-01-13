# 77. Combinations
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int):
        numbers = [i + 1 for i in range(n)]
        return list(combinations(numbers, k))

    def combine_dfs(self, n, k):
        result = []

        def dfs(element, start, k):
            if k == 0:
                result.append(element[:])

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                element.append(i)
                dfs(element, i + 1, k - 1)
                element.pop()

        dfs([], 1, k)
        return result


sol = Solution()
print(sol.combine(4, 2))
print(sol.combine_dfs(4, 2))
