from functools import reduce


class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        result = []
        point_left = 1
        for i in range(0, len(nums)):
            result.append(point_left)
            point_left *= nums[i]

        point_right = 1
        for i in reversed(range(len(nums))):
            result[i] *= point_right
            point_right *= nums[i]

        return result


class Solution2:
    def product_except_self(self, nums: [int]) -> [int]:
        result = []
        stack = []
        stack.extend(nums)
        for i in range(len(nums)):
            stack.remove(nums[i])
            multi = reduce(lambda x, y: x * y, stack)
            result.append(multi)
            stack.insert(i, nums[i])
        return result


nums1 = [1, 2, 3, 4]
nums2 = [4, 5]
sol = Solution()
sol2 = Solution2()
print(sol.productExceptSelf(nums1))
print(sol.productExceptSelf(nums2))
print(sol2.product_except_self(nums1))
print(sol2.product_except_self(nums2))
