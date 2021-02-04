# 33. Search in Rotated Sorted Array
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 최솟값 찾기
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # 피벗 기준 이진 검색
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1


sol = Solution()
nums1 = [4, 5, 6, 7, 0, 1, 2]
print(sol.search(nums1, 4))
