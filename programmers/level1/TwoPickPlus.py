from itertools import combinations


def solution(numbers):
    answer = []
    list_numbers = combinations(numbers, 2)

    for i in list_numbers:
        answer.append(sum(i))
    answer = list(set(answer))
    answer.sort()
    return answer


numbers1 = [2, 1, 3, 4, 1]
numbers2 = [5, 0, 2, 7]
print(solution(numbers1))
print(solution(numbers2))
