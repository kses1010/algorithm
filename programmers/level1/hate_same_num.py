# 같은 숫자는 싫어

def solution(arr: [int]) -> [int]:
    answer = [arr[0]]
    if len(arr) == 1:
        return arr[0]

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])
    return answer


arr1 = [1, 1, 3, 3, 0, 1, 1]
arr2 = [4, 4, 4, 3, 3]
print(solution(arr1))
print(solution(arr2))
