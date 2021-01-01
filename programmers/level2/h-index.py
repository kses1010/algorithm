# H-Index

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    count = 0

    for i in range(0, len(citations) + 1):
        for j in citations:
            if i <= j:
                count += 1
            if i == count:
                answer = i
        count = 0

    return answer


citations1 = [3, 0, 6, 1, 5]
citations2 = [5, 5, 5, 5]
print(solution(citations1))
print(solution(citations2))
