# 볼링공 고르기
from itertools import combinations


def solution(balls):
    ball_list = list(combinations(balls, 2))
    answer = [i for i in ball_list if i[0] != i[1]]
    return len(answer)


def solution2(balls):
    n = len(balls)
    # 공 무게 리스트(1 ~ 10)
    array = [0] * 11
    for i in balls:
        # 각 무게에 해당하는 볼링공의 개수 카운트
        array[i] += 1
    result = 0

    # 공의 최고무게
    m = max(balls)
    # 1부터 m 까지의 각 무게에 대하여 처리
    for i in range(1, m + 1):
        # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
        n -= array[i]
        # B가 선택하는 경우의 수와 곱하기
        result += array[i] * n
    return result


balls1 = [1, 3, 2, 3, 2]
balls2 = [1, 5, 4, 3, 2, 4, 5, 2]
print(solution(balls1))
print(solution2(balls1))
print(solution(balls2))
print(solution2(balls2))
