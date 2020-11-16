# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = []
    for x in moves:
        for y in range(len(board)):
            if board[y][x - 1] != 0:
                basket.append(board[y][x - 1])
                board[y][x - 1] = 0
                if basket[-1:] == basket[-2:-1]:
                    answer += 2
                    basket = basket[:-2]
                break
    return answer


board1 = [[0, 0, 0, 0, 0],
          [0, 0, 1, 0, 3],
          [0, 2, 5, 0, 1],
          [4, 2, 4, 4, 2],
          [3, 5, 1, 3, 1]]
moves1 = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board1, moves1))
# print(moves1[-2:-1], moves1[-1:])
