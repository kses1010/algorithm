# 개미 전사

def solution(arr):
    d = [0] * 101
    n = len(arr)
    d[0], d[1] = arr[0], max(arr[0], arr[1])
    for i in range(2, n):
        # d[i - 1] 은 현재 식량창고는 털 수 없기 때문에 K값(arr[i])을 더할 수 없다.
        d[i] = max(d[i - 1], d[i - 2] + arr[i])
    return d[n - 1]


arr1 = [1, 3, 1, 5]
print(solution(arr1))
