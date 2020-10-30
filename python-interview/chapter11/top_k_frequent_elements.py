import collections


class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        counter = collections.Counter(nums).most_common(k)
        answer = [k for k, v in counter]

        return answer

    def pythonic_way_sol(self, nums: [int], k: int) -> [int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]


nums1, k1 = [1, 1, 1, 2, 2, 3], 2
nums2, k2 = [1], 1

sol = Solution()
print(sol.topKFrequent(nums1, k1))
print(sol.pythonic_way_sol(nums1, k1))
print(sol.topKFrequent(nums2, k2))
