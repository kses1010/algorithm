# 구명보트

def solution(people, limit):
    # 구명보트 하나당 한사람이 탈 경우
    answer = len(people)
    people.sort()

    # 무게가 가장 많은 사람
    right = len(people) - 1
    for left in range(len(people)):
        # 제일 가벼운사람과 무거운 사람이 동시에 탔을 때 제한이 걸리지 않은 경우 보트 수 -1
        while left < right:
            if people[left] + people[right] <= limit:
                answer -= 1
                right -= 1
                break
            else:
                right -= 1

    return answer


people1, limit1 = [70, 50, 80, 50], 100
people2, limit2 = [70, 50, 80], 100
print(solution(people1, limit1))
print(solution(people2, limit2))
