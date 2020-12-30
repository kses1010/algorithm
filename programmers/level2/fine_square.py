# 멀쩡한 사각형
from math import gcd


def solution(w, h):
    # 전체 - (gcd * ((w // gcd + h // gcd) - 1))
    # 최대공약수가 1이면 w + h - 1을 해야 잘라지는 사각형의 갯수가 나온다.
    return w * h - (w + h - gcd(w, h))


print(solution(8, 12))
