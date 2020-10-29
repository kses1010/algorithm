def solution(n: int, lost: [int], reserve: [int]) -> int:
    answer = 0
    reser_del = set(reserve) - set(lost)
    lost_del = set(lost) - set(reserve)

    for i in reser_del:
        if i - 1 in lost_del:
            lost_del.remove(i - 1)
        elif i + 1 in lost_del:
            lost_del.remove(i + 1)

    answer = n - len(lost_del)
    return answer


n1, lost1, reserve1 = 5, [2, 5], [1, 3, 5]
n2, lost2, reserve2 = 5, [2, 4], [3]
n3, lost3, reserve3 = 3, [3], [1]

print(solution(n1, lost1, reserve1))
print(solution(n2, lost2, reserve2))
print(solution(n3, lost3, reserve3))
