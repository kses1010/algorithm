# 최솟값 만들기

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = []
    for a, b in zip(A, B):
        answer.append(a * b)
    return sum(answer)


a1, b1 = [1, 4, 2], [5, 4, 4]
a2, b2 = [1, 2], [3, 4]
print(solution(a1, b1))
print(solution(a2, b2))
