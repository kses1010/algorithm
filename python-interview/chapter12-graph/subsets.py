# 78. Subsets
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(index, path_list):
            answer.append(path_list)

            for i in range(index, len(nums)):
                dfs(i + 1, path_list + [nums[i]])

        dfs(0, [])
        return answer


sol = Solution()
nums1 = [1, 2, 3]
print(sol.subsets(nums1))
