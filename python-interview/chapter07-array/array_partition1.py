# 561. Array Partition I

class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        return sum(sorted(nums)[::2])

    def my_pair_sum(self, nums):
        nums.sort()
        return sum(nums[::2])


nums1 = [1, 4, 3, 2]
nums2 = [6, 2, 6, 5, 1, 2]
sol = Solution()
print(sorted(nums1))
print(sorted(nums1)[::2])
print(sorted(nums2)[::2])
print(sol.arrayPairSum(nums1))
print(sol.my_pair_sum(nums2))
