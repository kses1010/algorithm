# 가장 큰 정사각형 찾기


def solution(board):
    answer = []
    n, m = len(board), len(board[0])
    # 1부터 시작한 이유는 x좌표, y좌표가 0이면 어차피 정사각형 판정하기 어렵기 때문(좌표에서 벗어나기 때문)
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j - 1], min(board[i - 1][j], board[i][j - 1])) + 1
    for i in range(n):
        answer.append(max(board[i]))

    return max(answer) ** 2


def solution2(board):
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if i == 0 or j == 0:
                continue
            if board[i][j] != 0:
                board[i][j] = min(board[i - 1][j - 1], min(board[i - 1][j], board[i][j - 1])) + 1
    answer = []
    for i in range(row):
        answer.append(max(board[i]))
    return max(answer) ** 2


board1 = [[0, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [0, 0, 1, 0]]

board2 = [[0, 0, 1, 1],
          [1, 1, 1, 1]]

print(solution(board2))
print(solution(board1))
