# 내적

def solution(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])


a1, b1 = [1, 2, 3, 4], [-3, -1, 0, 2]
a2, b2 = [-1, 0, 1], [1, 0, -1]
print(solution(a1, b1))
print(solution(a2, b2))
