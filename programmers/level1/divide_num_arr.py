# 나누어 떨어지는 숫자 배열

def solution(arr: [int], divisor: int) -> [int]:
    answer = []
    for i, v in enumerate(arr):
        num, rest = divmod(v, divisor)
        if rest == 0:
            answer.append(v)

    if not answer:
        answer.append(-1)
        return answer
    answer.sort()
    return answer


arr1, divisor1 = [5, 9, 7, 10], 5
arr2, divisor2 = [2, 36, 1, 3], 1
arr3, divisor3 = [3, 2, 6], 10
print(solution(arr1, divisor1))
print(solution(arr2, divisor2))
print(solution(arr3, divisor3))
