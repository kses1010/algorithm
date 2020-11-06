# 문자열 내 마음대로 정렬하기

def solution(strings, n: int):
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer


strings1, n1 = ["sun", "bed", "car"], 1
strings2, n2 = ["abcd", "abce", "cdx"], 2
print(solution(strings1, n1))
print(solution(strings2, n2))
