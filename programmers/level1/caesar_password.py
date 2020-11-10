# 시저 암호
import string


def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return "".join(s)


def solution2(s, n):
    low = "abcdefghijklmnopqrstuvwxyz"  # 소문자. 인덱스는 0에서 25
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for char in s:
        if char in low:
            ind = low.find(char) + n  # low 문자열에서 찾은 해당 알파벳 인덱스 + n
            answer += low[ind % 26]  # 26으로 나눈 나머지를 사용할 경우 25를 초과하는 경우도 활용 가능
        elif char in up:
            ind = up.find(char) + n
            answer += up[ind % 26]
        else:  # 공백일 경우도 고려
            answer += " "
    return answer


def solution3(s, n):
    result = ""
    base = ""
    for c in s:
        if c in string.ascii_lowercase:
            base = string.ascii_lowercase
        elif c in string.ascii_uppercase:
            base = string.ascii_uppercase
        else:
            result += c
            continue
        a = base.index(c) + n
        result += base[a % len(base)]
    return result


s1, n1 = "AB", 1
s2, n2 = "z", 1
s3, n3 = "a B z", 4
print(solution(s1, n1))
print(solution2(s1, n1))
print(solution3(s1, n1))
