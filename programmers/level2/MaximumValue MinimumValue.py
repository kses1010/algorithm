# 최댓값과 최솟값

def solution(s):
    number_list = list(map(int, s.split(' ')))
    max_num = str(max(number_list))
    min_num = str(min(number_list))

    return min_num + " " + max_num


s1 = "1 2 3 4"
s2 = "-1 -2 -3 -4"
print(solution(s1))
print(solution(s2))
