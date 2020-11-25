# 피보나치 함수

# 재귀로 푸는 피보나치
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))

# 캐싱을 이용하여 재귀 피보나치
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100


# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo_cache(x):
    # 종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo_cache(x - 1) + fibo_cache(x - 2)
    return d[x]


print(fibo_cache(9))


def fibo_for(x):
    d1 = [0] * 100
    d1[1], d1[2] = 1, 1
    for i in range(3, x + 1):
        d1[i] = d1[i - 1] + d1[i - 2]
    return d[x]


print(fibo_for(9))


