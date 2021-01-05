# 1. Two Sum

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution2:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i, v in enumerate(nums):
            rest_num = target - v

            if rest_num in nums[i + 1:]:
                return nums.index(v), nums[i + 1:].index(rest_num) + (i + 1)


class Solution3:
    def twoSum(self, nums: [int], target: int) -> [int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i


# 사실상 이진 탐색
class Solution4:
    def twoSum(self, nums: [int], target: int) -> [int]:
        left = 0
        right = len(nums) - 1
        while not left == right:
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]


nums1 = [2, 7, 11, 15]
target1 = 9

nums2 = [3, 2, 4]
target2 = 6

nums3 = [3, 3]
target3 = 6

sol = Solution()
print(sol.twoSum(nums1, target1))
print(sol.twoSum(nums2, target2))
print(sol.twoSum(nums3, target3))
print("-------------------------")
sol2 = Solution2()
print(sol2.twoSum(nums1, target1))
print(sol2.twoSum(nums2, target2))
print(sol2.twoSum(nums3, target3))
print("-------------------------")
sol3 = Solution3()
print(sol3.twoSum(nums1, target1))
print(sol3.twoSum(nums2, target2))
print(sol3.twoSum(nums3, target3))
print("-------------------------")
sol4 = Solution4()
print(sol4.twoSum(nums1, target1))
print(sol4.twoSum(nums2, target2))
print(sol4.twoSum(nums3, target3))
