# 럭키 스트라이크

def solution(n):
    point = str(n)
    pivot = len(point) // 2
    left = point[0:pivot]
    right = point[pivot:len(point)]
    left_sum = sum([int(i) for i in left])
    right_sum = sum([int(i) for i in right])
    if left_sum == right_sum:
        return 'LUCKY'
    return 'READY'


print(solution(123402))
print(solution(7755))
