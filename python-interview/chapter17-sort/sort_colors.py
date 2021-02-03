# 75. Sort Colors
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()

    def nederland_sort(self, nums):
        # red = 0, white = 1, blue = 2
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1


sol = Solution()
nums1 = [2, 0, 2, 1, 1, 0]
sol.sortColors(nums1)
print(nums1)
