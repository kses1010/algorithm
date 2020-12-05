# 곱하기 혹은 더하기

def solution(s):
    answer = int(s[0])
    for i in range(1, len(s)):
        if int(s[i - 1]) == 0 or int(s[i - 1]) == 1:
            answer += int(s[i])
        else:
            answer *= int(s[i])
    return answer


print(solution('02984'))
print(solution('567'))
