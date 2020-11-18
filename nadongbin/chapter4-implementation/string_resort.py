# 문자열 재졍렬

def solution(strs):
    alpha = []
    number = []
    for i in strs:
        if i.isalpha():
            alpha.append(i)
        else:
            number.append(int(i))
    alpha.sort()
    strings = ''.join(alpha)
    return strings + str(sum(number))


str1 = "K1KA5CB7"
print(solution(str1))
