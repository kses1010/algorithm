# 가장 큰 수

def solution(numbers):
    num_strs = list(map(str, numbers))
    num_strs.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(num_strs)))


numbers1 = [6, 10, 2]
numbers2 = [3, 31, 34, 5, 9]
numbers3 = [9, 991]
print(solution(numbers1))
print(solution(numbers2))
print(solution(numbers3))
