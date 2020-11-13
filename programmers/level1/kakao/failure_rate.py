# 실패율


def solution(N, stages):
    result = {}
    user_num = len(stages)
    for i in range(1, N + 1):
        if user_num != 0:
            count = stages.count(i)
            result[i] = count / user_num
            user_num -= count
        else:
            result[i] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)


N1, stages1 = 5, [2, 1, 2, 6, 2, 4, 3, 3]
N2, stages2 = 4, [4, 4, 4, 4, 4]
print(solution(N1, stages1))
print(solution(N2, stages2))
