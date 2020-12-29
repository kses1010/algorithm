# 2110 - 공유기 설치

def solution(arr, c):
    arr.sort()
    # start, end 값은 집 좌표값이 아닌 gap 값
    start = 1
    end = arr[-1] - arr[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        router = arr[0]
        count = 1
        # 현재의 mid 값을 이용하여 공유기를 설치
        for i in range(1, len(arr)):
            # 설치된 공유기와 거리보다 같거나 크면
            if arr[i] >= router + mid:
                # router 를 설치.
                router = arr[i]
                count += 1
        # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        if count >= c:
            start = mid + 1
            result = mid
        # C개 이상의 공유기를 설치할 수 없는 경우, 거리 감소
        else:
            end = mid - 1
    return result


arr1 = [1, 2, 8, 4, 9]
n1 = 3
print(solution(arr1, n1))
