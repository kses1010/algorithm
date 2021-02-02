# 215. Kth Largest Element in an Array
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

    def find_kth_largest(self, nums, k):
        return heapq.nlargest(k, nums)


sol = Solution()
list1 = [3, 2, 1, 5, 6, 4]
list2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(sol.findKthLargest(list1, 2))
# print(sol.findKthLargest(list2, 4))
print(sol.find_kth_largest(list2, 4))
