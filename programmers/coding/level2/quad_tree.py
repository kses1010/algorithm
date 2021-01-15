# 쿼드압축 후 개수 세기


def solution(arr):
    answer = [0, 0]
    n = len(arr)

    def dfs(x, y, n):
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != arr[x][y]:
                    next_n = n // 2
                    dfs(x, y, next_n)
                    dfs(x, y + next_n, next_n)
                    dfs(x + next_n, y, next_n)
                    dfs(x + next_n, y + next_n, next_n)
                    return

        answer[arr[x][y]] += 1

    dfs(0, 0, n)
    return answer


arr1 = [[1, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 1]]
arr2 = [[0, 0],
        [0, 0]]

print(solution(arr2))
