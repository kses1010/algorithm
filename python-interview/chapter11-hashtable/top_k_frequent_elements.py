# 347. Top K Frequent Elements

import collections
import heapq


class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        counter = collections.Counter(nums).most_common(k)
        answer = [k for k, v in counter]

        return answer

    # 우선순위 큐를 활용한 풀이법
    def top_k_heapq(self, nums, k):
        counter = collections.Counter(nums)
        q = []
        for i in counter:
            heapq.heappush(q, (-counter[i], i))
        answer = [heapq.heappop(q)[1] for _ in range(k)]
        return answer

    def pythonic_way_sol(self, nums: [int], k: int) -> [int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]


nums1, k1 = [1, 1, 1, 2, 2, 3], 2
nums2, k2 = [1], 1

sol = Solution()
print(sol.topKFrequent(nums1, k1))
print(sol.pythonic_way_sol(nums1, k1))
print(sol.top_k_heapq(nums1, k1))
