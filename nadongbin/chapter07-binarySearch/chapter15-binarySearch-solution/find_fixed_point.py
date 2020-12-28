# 고정점 찾기

def solution(arr):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return -1


arr1 = [-15, -6, 1, 3, 7]
arr2 = [-15, -4, 2, 8, 9, 13, 15]
arr3 = [-15, -4, 3, 8, 9, 13, 15]
print(solution(arr1))
print(solution(arr2))
print(solution(arr3))
