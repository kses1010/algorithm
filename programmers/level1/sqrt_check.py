# 정수 제곱근 판별
import math


def solution(n):
    num = math.sqrt(n)
    if num.is_integer():
        return int((num + 1) ** 2)
    return -1


print(solution(121))
print(solution(3))
