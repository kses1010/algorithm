# 124나라의 숫자

def solution(n):
    dict_num = {1: '1', 2: '2', 3: '4'}
    if n <= 3:
        return dict_num[n]
    else:
        # 삼진법에는 0이 포함되지 않으므로 n - 1로 나눈다.
        q, r = divmod(n - 1, 3)
        return solution(q) + dict_num[r + 1]


for i in range(1, 15):
    print(i, solution(i))
