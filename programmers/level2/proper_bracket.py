# 올바른 괄호

def solution(s):
    stack = []
    for i in s:
        if i == ")":
            if not stack:
                return False
            else:
                stack.pop()
        else:
            stack.append(i)

    if stack:
        return False
    return True


print(solution("()()"))
print(solution("(())"))
