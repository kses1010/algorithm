# 1이 될 때까지

def solution(n, k):
    result = 0
    while True:
        target = (n // k) * k
        result += (n - target)
        n = target
        if n < k:
            break
        result += 1
        n //= k

    result += (n - 1)
    return result


print(solution(25, 5))
