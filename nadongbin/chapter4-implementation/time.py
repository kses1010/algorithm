# 시각

def solution(n):
    answer = 0
    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    answer += 1
    return answer


print(solution(5))
