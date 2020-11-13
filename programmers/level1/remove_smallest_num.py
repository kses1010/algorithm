# 제일 작은 수 제거하기

def solution(arr):
    arr.pop(arr.index(min(arr)))
    if not arr:
        arr.append(-1)
    return arr


arr1, arr2 = [4, 3, 2, 1], [10]
print(solution(arr1))
print(solution(arr2))
