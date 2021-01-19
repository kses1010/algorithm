# 땅따먹기

# 런타임 에러 발생 아무래도 land사이즈가 커지면 에러나는듯
def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    index = -1
    for i in range(n):
        score = max(land[i])
        if land[i].index(score) != index:
            answer += score
            index = land[i].index(score)
        else:
            land[i].pop(land[i].index(score))
            score = max(land[i])
            answer += score
            index = land[i].index(score)

    return answer


def solution2(land):
    for i in range(0, len(land) - 1):
        land[i + 1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i + 1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i + 1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i + 1][3] += max(land[i][0], land[i][1], land[i][2])

    return max(land[len(land) - 1])


# 다이나믹 프로그래밍
def dynamic(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            # 똑같은 열의 숫자를 제외하는 식
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
    return max(land[-1])


land1 = [[1, 2, 3, 5],
         [5, 6, 7, 8],
         [4, 3, 2, 1]]

# print(solution(land1))
# print(solution2(land1))
print(dynamic(land1))
