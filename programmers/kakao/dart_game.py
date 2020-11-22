# 다트 게임
import re


def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'*': 2, '#': -1}

    score = [0, 0, 0]
    point = -1

    for i, v in enumerate(dartResult):
        if v.isdecimal():
            point += 1
            if v == '0':
                continue
            elif dartResult[i + 1].isdecimal():
                score[point] = int(v) * 10
                point -= 1
            else:
                score[point] = int(v)

        elif v in 'SDT':
            score[point] **= bonus[v]
        else:
            if v == '*':
                score[point - 1] *= 2

            score[point] *= option[v]

    return sum(score)


def solution2(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}

    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)

    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


dartResult1 = '1S2D*3T'
dartResult2 = '1D2S#10S'

print(solution(dartResult1))
print(solution2(dartResult2))
