# 효율적인 화폐 구성

def solution(money, coin):
    # DP 테이블 초기화 10001은 INF 대신 사용
    d = [10001] * (money + 1)
    d[0] = 0

    num = len(coin)
    for k in range(num):
        for j in range(coin[k], money + 1):
            # (money - k)원을 만드는 방법이 존재하는 경우
            if d[j - coin[k]] != 10001:  # 이 조건문은 삭제해도 무방. 최소값은 10001보다 작기 때문
                d[j] = min(d[j], d[j - coin[k]] + 1)
    if d[money] == 10001:
        return -1

    return d[money]


money1, coin1 = 15, [2, 3]
money2, coin2 = 4, [3, 5, 7]
print(solution(money1, coin1))
print(solution(money2, coin2))
