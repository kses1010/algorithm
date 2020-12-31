# 삼각형 달팽이

def solution(n):
    answer = []
    maps = [[0] * n for _ in range(n)]
    x, y = -1, 0
    num = 1

    for i in range(n):
        for _ in range(i, n):

            # Down
            if i % 3 == 0:
                x += 1

            # Right
            elif i % 3 == 1:
                y += 1

            # Up & Left
            elif i % 3 == 2:
                x -= 1
                y -= 1

            maps[x][y] = num
            num += 1

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 0:
                answer.append(maps[i][j])

    return answer


print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
