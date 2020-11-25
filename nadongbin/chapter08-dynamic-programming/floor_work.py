# 바닥 공사

def solution(n):
    d = [0] * 1000
    d[1], d[2] = 1, 3
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + d[i - 2] * 2) % 796796
    return d[n]


print(solution(2))
print(solution(3))
print(solution(4))
