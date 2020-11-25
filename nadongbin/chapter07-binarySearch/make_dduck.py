# 떡볶이 떡 만들기

def solution(arr, m):
    start, end = 0, max(arr)
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in arr:
            # 잘랐을 때의 떡의 양 계산
            if i > mid:
                total += i - mid
        # 떡의 양이 부족한 경우 더 많이 자르기
        if total < m:
            end = mid - 1
        else:
            # 최대한 덜 잘랐을 때가 정답.
            result = mid
            start = mid + 1
    return result


arr1, m1 = [19, 15, 10, 17], 6
print(solution(arr1, m1))
