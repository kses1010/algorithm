# 가운데 글자 가져오기

def solution(s: str) -> str:
    m = len(s) // 2
    if len(s) % 2 == 0:
        return s[m]
    return s[m:m + 2]
