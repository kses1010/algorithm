# 하샤드 수

def solution(x):
    num = sum(int(i) for i in str(x))
    if x % num == 0:
        return True
    return False


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))
