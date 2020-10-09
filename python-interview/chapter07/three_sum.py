class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        result = []
        nums.sort()
        if len(nums) < 3:
            return result

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append((nums[i], nums[j], nums[k]))

        return result


class Solution2:
    def threeSum(self, nums: [int]) -> [[int]]:
        result = []
        nums.sort()
        if len(nums) < 3:
            return result

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append((nums[i], nums[left], nums[right]))

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result


nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = []
nums3 = [1, -1, -1, 0]
sol = Solution()
sol2 = Solution2()
print(sol.threeSum(nums1))
print(sol.threeSum(nums2))
print(sol.threeSum(nums3))
print('-------------')
print(sol2.threeSum(nums1))
print(sol2.threeSum(nums2))
print(sol2.threeSum(nums3))
