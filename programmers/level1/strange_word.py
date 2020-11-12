# 이상한 문자 만들기

def solution(s):
    answer = ''
    idx = 0
    for i in s:
        if i.isalpha():
            if idx % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
            idx += 1
        else:
            idx = 0
            answer += ' '
    return answer


s1 = "try hello world"
print(solution(s1))
