# 부품 찾기

def solution(n, arr_n, m, arr_m):
    answer = []
    for i in arr_m:
        if i in arr_n:
            answer.append("yes")
        else:
            answer.append("no")
    return answer


# 이진 탐색
def bs_solution(arr_n, arr_m):
    def binary_search(arr, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return None

    answer = []
    for i in arr_m:
        result = binary_search(arr_n, i, 0, len(arr_n) - 1)
        if result is not None:
            answer.append('yes')
        else:
            answer.append('no')
    return answer


# 계수 정렬
def count_solution(arr1, arr2):
    arr_count = [0] * 1000001
    for i in arr1:
        arr_count[int(i)] = 1

    answer = []
    for i in arr2:
        if arr_count[i] == 1:
            answer.append('yes')
        else:
            answer.append('no')
    return answer

# 집합 자료형 set
def set_solution(arr1, arr2):
    set_list = set(arr1)
    answer = []
    for i in arr2:
        if i in set_list:
            answer.append('yes')
        else:
            answer.append('no')
    return answer


n1, arr_n1 = 5, [8, 3, 7, 9, 2]
m1, arr_m1 = 3, [5, 7, 9]
print(solution(n1, arr_n1, m1, arr_m1))
print(bs_solution(arr_n1, arr_m1))
print(count_solution(arr_n1, arr_m1))
print(set_solution(arr_n1, arr_m1))
