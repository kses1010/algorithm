# 기능 개발
import math


def solution(progresses, speeds):
    answer = []
    rest_work = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]

    # 위 리스트는 다음 로직처럼 풀어쓴 것을 zip함수로 처리함.
    # rest_work = []
    # for i in range(len(progresses)):
    #     complete_day = math.ceil((100 - progresses[i]) / speeds[i])
    #     rest_work.append(complete_day)

    prior = 0
    for i in range(len(rest_work)):
        # 인덱스의 남은 일정이 그 뒤 일정보다 작으면 그 만큼 빼고 answer 에 추가.
        if rest_work[prior] < rest_work[i]:
            answer.append(i - prior)
            prior = i  # 일정 인덱스로 변경

    # 남은 일정 추가
    answer.append(len(rest_work) - prior)
    return answer


progress1, speed1 = [93, 30, 55], [1, 30, 5]
progress2, speed2 = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]
print(solution(progress1, speed1))
print(solution(progress2, speed2))
