class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        return sum(sorted(nums)[::2])


nums = [1, 4, 3, 2]
sol = Solution()
print(sorted(nums))
print(sorted(nums)[::2])
print(sol.arrayPairSum(nums))
