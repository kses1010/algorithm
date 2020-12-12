# 괄호 변환

def check_bracket(text):  # 균형잡혔을 때, 올바른지 체크,
    left = 0
    right = 0
    for bracket in text:
        if bracket == '(':
            left += 1
        else:
            right += 1
        if left < right:
            return False
    return True


def divide_bracket(p):
    if p == '':
        return ''
    left = 0
    right = 0
    last = ''

    for index in range(len(p)):
        if p[index] == '(':
            left += 1
        else:
            right += 1
        last = p[index]
        if left == right:
            if last == ')':  # 수가 같은데 닫혔으면 올바르다.
                # u가 올바르면 # 뒤에도 똑같이 진행하면 된다. 그 값을 더해서 반환
                return p[:index + 1] + divide_bracket(p[index + 1:])
            else:  # 안 올바르다 균형은 잡혔다.
                # 앞에꺼 올바르게 고치기 -> 뒤에꺼 나누기
                return reverse(p[:index + 1], divide_bracket(p[index + 1:]))


def reverse(u, v):  # 앞 뒤 뒤집어서 v 붙여서 더함. v도 다 마친 상태.
    empty = '('
    empty += v + ')'
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            empty += ')'
        else:
            empty += '('
    return empty


def solution(p):
    if check_bracket(p):
        return p

    return divide_bracket(p)


p1 = "(()())()"
p2 = ")("
p3 = "()))((()"
print(solution(p1))
print(solution(p3))
print(solution(p2))
