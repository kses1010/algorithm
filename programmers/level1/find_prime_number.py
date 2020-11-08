# 소수 찾기

def solution(n):
    sieve = [True] * (n + 1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(2 * i, n + 1, i):
                sieve[j] = False

    return len([i for i in range(2, n + 1) if sieve[i]])


print(solution(5))
print(solution(10))
