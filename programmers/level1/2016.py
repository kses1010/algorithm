# 2016년

def solution(a: int, b: int) -> str:
    date = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day_sum = 0
    for i in range(a):
        day_sum += date[i]

    day_sum += b
    answer = day[(day_sum % 7) - 1]
    return answer


print(solution(1, 1))
print(solution(5, 24))
