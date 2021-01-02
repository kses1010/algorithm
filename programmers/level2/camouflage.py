# 위장

def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 2
    count = 1
    for i in answer.values():
        count *= i
    return count - 1


clothes1 = [['yellow_hat', 'headgear'],
            ['green_turban', 'headgear'],
            ['blue_sunglasses', 'eye_wear']]

print(solution(clothes1))
