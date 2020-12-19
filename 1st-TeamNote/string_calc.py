# 문자열 계산기


def compare_op(op1, op2):
    op_dict = {'+': 2, '-': 2, '*': 3, '/': 3, '(': 1}
    return op_dict[op1] - op_dict[op2]


def convert_postfix(s):
    str_list = [i for i in s if i != ' ']
    stack = []
    postfix = []

    for i in range(len(str_list)):
        if str_list[i].isdigit():
            postfix.append(str_list[i])
        else:
            if str_list[i] == '(':
                stack.append(str_list[i])
            elif str_list[i] == ')':
                while True:
                    pop_op = stack.pop()
                    if pop_op == '(':
                        break
                    postfix.append(pop_op)
            elif str_list[i] in '+-*/':
                while stack and compare_op(stack[-1], str_list[i]) >= 0:
                    postfix.append(stack.pop())

                stack.append(str_list[i])
    while stack:
        postfix.append(stack.pop())
    return postfix


def calculate(s):
    input_list = convert_postfix(s)
    stack = []

    for i in range(len(input_list)):
        if input_list[i].isdigit():
            stack.append(int(input_list[i]))
        else:
            num2 = stack.pop()
            num1 = stack.pop()

            if input_list[i] == '+':
                stack.append(num1 + num2)
            elif input_list[i] == '-':
                stack.append(num1 - num2)
            elif input_list[i] == '*':
                stack.append(num1 * num2)
            else:
                stack.append(num1 / num2)

    return stack.pop()


s1 = '1 + 2 * 3 + 4'
print(convert_postfix(s1))
print(calculate(s1))
