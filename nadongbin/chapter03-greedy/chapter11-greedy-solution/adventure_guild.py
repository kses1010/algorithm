# 모험가 길드

def solution(n):
    n.sort()
    group = 0
    count = 0
    for i in n:
        count += 1
        if count >= i:
            group += 1
            count = 0
    return group


n1 = [2, 3, 1, 2, 2]
print(solution(n1))
