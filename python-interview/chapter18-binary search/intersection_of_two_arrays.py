# 349. Intersection of Two Arrays
import bisect
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums2)
        nums2_set = set(nums1)

        answer = []
        for i in nums1_set:
            if i in nums2_set:
                answer.append(i)

        return answer

    def bs_intersection(self, nums1, nums2):
        result = set()
        nums2.sort()
        for i1 in nums1:
            i2 = bisect.bisect_left(nums2, i1)
            if len(nums2) > 0 and len(nums2) > i2 and i1 == nums2[i2]:
                result.add(i1)
        return result


nums1, nums2 = [1, 2, 2, 1], [2, 2]
nums3, nums4 = [4, 9, 5], [9, 4, 9, 8, 4]
sol = Solution()
print(sol.intersection(nums1, nums2))
print(sol.intersection(nums3, nums4))
print(sol.bs_intersection(nums1, nums2))
print(sol.bs_intersection(nums3, nums4))
