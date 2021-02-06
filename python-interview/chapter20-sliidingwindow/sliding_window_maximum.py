# 239. Sliding Window Maximum
from collections import deque
from math import inf
from typing import List


class Solution:
    # 시간 초과
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []

        for i in range(len(nums) - k + 1):
            answer.append(max(nums[i:i + k]))
        return answer

    # 이것도 시간 초과
    def max_sliding_window(self, nums, k):
        answer = []
        window = deque()
        current_max = -inf
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if current_max == -inf:
                current_max = max(window)
            elif v > current_max:
                current_max = v

            answer.append(current_max)

            # 최댓값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = -inf
        return answer

    def max_slide_window(self, nums, k):
        # 인덱스 저장
        index_q = deque()
        answer = []

        for i, cur in enumerate(nums):
            # 큐에서 현재 값보다 작은값은 제거.
            while index_q and nums[index_q[-1]] <= cur:
                index_q.pop()
            index_q.append(i)

            # 윈도우사이즈보다 크면, 맨 왼쪽 제거.
            if index_q[0] == i - k:
                index_q.popleft()
            # 윈도우 사이즈에 맞을 때 값 추가
            if i >= k - 1:
                answer.append(nums[index_q[0]])
        return answer


sol = Solution()
nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
nums2 = [1]
nums3 = [1, -1]
nums4 = [2, 4, 7]
print(sol.maxSlidingWindow(nums1, 3))
# print(sol.maxSlidingWindow(nums2, 1))
# print(sol.maxSlidingWindow(nums3, 1))
# print(sol.maxSlidingWindow(nums4, 2))
print(sol.max_sliding_window(nums1, 3))
print(sol.max_slide_window(nums1, 3))
