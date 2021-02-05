# 136. Single Number
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in nums:
            answer ^= i
        return answer


sol = Solution()
nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
print(sol.singleNumber(nums1))
print(sol.singleNumber(nums2))
