# 타겟 넘버


def solution(numbers, target):
    n = len(numbers)
    count = 0

    # dfs 트리층, 합계
    def dfs(layer, total):
        if layer == n:
            if total == target:
                nonlocal count
                count += 1
        else:
            # 마지막 노드까지 못갔다면 dfs 재귀
            dfs(layer + 1, total + numbers[layer])  # + 연산
            dfs(layer + 1, total - numbers[layer])  # - 연산

    dfs(0, 0)
    return count


numbers1, target1 = [1, 1, 1, 1, 1], 3
print(solution(numbers1, target1))
