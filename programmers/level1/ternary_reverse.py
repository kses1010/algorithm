# 삼진법 뒤집기

def solution(n) -> int:
    def n_ary(num, base):
        result = []
        while num > 0:
            num, r = divmod(num, base)
            result.append(r)
        return ''.join(map(str, reversed(result)))

    answer = n_ary(n, 3)
    answer = answer[::-1]
    return int(answer, 3)


print(solution(45))
print(solution(125))
print(solution(1000000))
