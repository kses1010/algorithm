# 퀵 정렬

def quick_sort(arr, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    # 피벗은 첫 번째 원소
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right - 1)
    quick_sort(arr, start + 1, end)


def quick_sort_py(arr):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr
    # 피벗은 첫 번째 원소
    pivot = arr[0]
    # 피벗을 제외한 리스트
    tail = arr[1:]

    # 분할된 왼쪽 부분
    left_side = [i for i in tail if i <= pivot]
    # 분할된 오른쪽 부분
    right_side = [i for i in tail if i > pivot]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행, 전체 리스트 반환
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)


arr1 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
arr2 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(arr1, 0, len(arr1) - 1)
print(arr1)
print(quick_sort_py(arr2))
