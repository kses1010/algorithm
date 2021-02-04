# 704. Binary Search
import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

    def recur_search(self, nums, target):
        def _binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return _binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return _binary_search(left, mid - 1)
                else:
                    return mid

            else:
                return -1

        return _binary_search(0, len(nums) - 1)

    def search_while(self, nums, target):
        left, right = 0, len(nums - 1)
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


sol = Solution()
nums1 = [-1, 0, 3, 5, 9, 12]
print(sol.search(nums1, 10))
