# 소수 찾기

def check_prime_number(n):
    if n < 2:
        return False
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if n % i == 0:
            return False
    return True


# 에라토스테네스의 체
def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            j = 2
            while i * j <= n:
                sieve[i * j] = False
                j += 1

    return len([i for i in range(2, n + 1) if sieve[i]])
