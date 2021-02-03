# 179. Largest Number
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(i) for i in nums]
        i = 1
        while i < len(str_nums):
            j = i
            while j > 0 and self.swap_check(str_nums[j - 1], str_nums[j]):
                str_nums[j], str_nums[j - 1] = str_nums[j - 1], str_nums[j]
                j -= 1
            i += 1

        return str(int(''.join(str_nums)))

    def swap_check(self, n1, n2):
        return n1 + n2 < n2 + n1


sol = Solution()
nums1 = [10, 2]
nums2 = [3, 30, 34, 5, 9]
nums3 = [3432, 34323]
# print(sol.largestNumber(nums1))
print(sol.largestNumber(nums2))
print(sol.largestNumber(nums3))
