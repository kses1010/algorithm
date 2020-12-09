# 문자열 재정렬

def solution(s):
    number = []
    alpha = []
    for i in s:
        if i.isdecimal():
            number.append(int(i))
        else:
            alpha.append(i)
    alpha.sort()
    return ''.join(alpha) + ''.join(str(sum(number)))


print(solution('K1KA5CB7'))
print(solution('AJKDLSI412K4JSJ9D'))
