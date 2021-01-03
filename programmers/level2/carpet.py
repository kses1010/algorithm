# 카펫


def solution(brown, yellow):
    x = 3
    while x <= brown:
        y = (yellow / (x - 2)) + 2
        if y == int(y):
            y = int(y)
            if (x + y - 2) * 2 == brown:
                return [max(x, y), min(x, y)]
        x += 1


print(solution(10, 2))
print(solution(14, 4))
print(solution(8, 1))
print(solution(24, 24))
