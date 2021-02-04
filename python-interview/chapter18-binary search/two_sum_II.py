# 167. Two Sum II - Input array is sorted
import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]

    def bs_two_sum(self, numbers, target):
        for k, v in enumerate(numbers):
            rest = target - v
            i = bisect.bisect_left(numbers, rest, k + 1)
            if i < len(numbers) and numbers[i] == rest:
                return k + 1, i + 1


sol = Solution()
nums = [2, 7, 11, 15]
print(sol.twoSum(nums, 9))
print(sol.bs_two_sum(nums, 9))
