# 더 맵게
import heapq


def solution(scoville, k):
    answer = 0
    q = scoville
    heapq.heapify(q)
    while q[0] < k:
        first = heapq.heappop(q)
        second = heapq.heappop(q)
        heapq.heappush(q, (first + (second * 2)))
        answer += 1
        if len(q) == 1 and q[0] < k:
            return -1
    return answer


scoville1, k1 = [1, 2, 3, 9, 10, 12], 7
print(solution(scoville1, k1))
