# 핸드폰 번호 가리기

def solution(phone_number):
    num = len(phone_number) - 4
    answer = "*" * num + phone_number[num:]
    return answer


p1, p2 = "01033334444", "027778888"
print(solution(p1))
print(solution(p2))
