# 예산

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)


d1, budget1 = [1, 3, 5, 2, 4], 9
d2, budget2 = [2, 2, 3, 3, 5], 10
print(solution(d1, budget1))
print(solution(d2, budget2))
