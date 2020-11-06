# 문자열 내 p와 y의 개수

def solution(s: str) -> bool:
    strs = list(s.lower())
    if 'p' not in strs and 'y' not in strs:
        return False

    count_p, count_y = 0, 0
    for i in strs:
        if i == 'p':
            count_p += 1
        elif i == 'y':
            count_y += 1
    if count_p == count_y:
        return True
    return False


def num_py(s):
    return s.lower().count('p') == s.lower().count('y')


s1, s2 = "pPoooyY", "Pyy"
print(solution(s1))
print(solution(s2))
print(solution("abc"))
