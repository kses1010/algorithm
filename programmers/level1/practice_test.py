from itertools import combinations


def solution(answers: [int]) -> [int]:
    answer = []
    a_count, b_count, c_count = 0, 0, 0
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if a[i % len(a)] == answers[i]:
            a_count += 1
        if b[i % len(b)] == answers[i]:
            b_count += 1
        if c[i % len(c)] == answers[i]:
            c_count += 1

    max_answer = max(a_count, b_count, c_count)
    if max_answer == a_count:
        answer.append(1)
    if max_answer == b_count:
        answer.append(2)
    if max_answer == c_count:
        answer.append(3)

    answer.sort()

    return answer


answers1 = [1, 2, 3, 4, 5]
answers2 = [1, 3, 2, 4, 2]
print(solution(answers1))
print(solution(answers2))
