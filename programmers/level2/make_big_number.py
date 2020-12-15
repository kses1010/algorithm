# 큰 수 만들기


def solution(number, k):
    stack = []

    for i in number:
        # 스택에 마지막에 넣었던 숫자보다 지금 넣을 숫자가 크다면 삭제
        while stack and i > stack[-1] and k != 0:
            stack.pop()
            k -= 1
        # 삭제후 추가
        stack.append(i)
    # 숫자를 전부 다넣었음에도 불구하고 k가 남은경우 k번 삭제
    while k > 0:
        stack.pop()
        k -= 1

    return ''.join(stack)


print(solution('1924', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))
