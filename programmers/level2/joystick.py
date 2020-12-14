# 조이스틱

def solution(name):
    alpha_lists = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]
    answer = 0
    index = 0
    while True:
        answer += alpha_lists[index]
        alpha_lists[index] = 0
        if sum(alpha_lists) == 0:
            break
        left, right = 1, 1
        while alpha_lists[index - left] == 0:
            left += 1
        while alpha_lists[index + right] == 0:
            right += 1

        answer += left if left < right else right
        index += -left if left < right else right

    return answer


print(solution('JAZ'))
print(solution('BCAAD'))
