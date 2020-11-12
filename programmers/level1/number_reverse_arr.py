# 자리수 뒤집어 배열로 만들기

def solution(n):
    return [int(i) for i in list(reversed(str(n)))]


print(solution(12345))


# 정수 내림차순으로 배치하기

def solution2(n):
    list_num = [int(i) for i in str(n)]
    list_num.sort(reverse=True)
    list_str = list(map(str, list_num))
    return int(''.join(list_str))


print(solution2(118372))
