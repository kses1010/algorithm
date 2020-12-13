# 소수 찾기
from itertools import permutations


def check_prime_number(n):
    if n < 2:
        return False
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = set()
    for i in range(1, len(numbers) + 1):
        num_list = list(map(''.join, permutations(list(numbers), i)))
        for j in list(set(num_list)):
            if check_prime_number(int(j)):
                answer.add(int(j))

    return len(answer)


print(solution('17'))
print(solution('011'))
