# 정렬된 배열에서 특정 수의 개수 구하기

import bisect


def solution(arr, n):
    left = bisect.bisect_left(arr, n)
    right = bisect.bisect_right(arr, n)
    if left == len(arr) and right == len(arr):
        return -1
    return right - left


arr1, n1 = [1, 1, 2, 2, 2, 2, 3], 2
print(solution(arr1, n1))
print(solution(arr1, 4))
print(solution(arr1, 3))
