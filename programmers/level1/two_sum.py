# 두 정수 사이의 합

def solution(a, b):
    n, m = max(a, b), min(a, b)
    num_list = [i for i in range(m, n + 1)]
    return sum(num_list)


print(solution(3, 5))
