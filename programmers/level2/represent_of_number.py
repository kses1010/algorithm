# 숫자의 표현

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        number = [i]
        target = sum(number)
        if target == n:
            answer += 1
        tmp = i
        while target < n:
            tmp += 1
            number.append(tmp)
            if sum(number) == n:
                print(number)
                answer += 1
            elif sum(number) > n:
                break
    return answer


print(solution(15))
print(solution(2))
