# 주식 가격

def solution(prices):
    answers = [0] * len(prices)
    stack = []
    for i, cur in enumerate(prices):
        while stack and cur < prices[stack[-1]]:
            last = stack.pop()
            answers[last] = i - last
        stack.append(i)
    print(stack)
    while stack:
        temp = stack.pop()
        answers[temp] = len(prices) - temp - 1
    return answers


prices1 = [1, 2, 3, 2, 3]
prices2 = [1, 2, 3]
print(solution(prices1))
