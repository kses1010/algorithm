# 게임 개발

def solution(n, m, avatar, maps):
    # 방문위치 초기화
    d = [[0] * m for _ in range(n)]

    # 현재 캐릭터의 x 좌표, y 좌표 입력받기
    y, x, direction = avatar[0], avatar[1], avatar[2]
    d[y][x] = 1

    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    # 왼쪽으로 회전
    def turn_left():
        nonlocal direction
        direction -= 1
        if direction == -1:
            direction = 3

    # 시뮬레이션 시작
    count = 1
    turn_time = 0
    while True:
        # 왼쪽으로 회전
        turn_left()
        ny = y + dy[direction]
        nx = x + dx[direction]
        # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
        if d[ny][nx] == 0 and maps[ny][nx] == 0:
            d[ny][nx] = 1
            y, x = ny, nx
            count += 1
            turn_time = 0
            continue
        # 가본곳이거나 바다인 경우
        else:
            turn_time += 1
        # 네 방향 모두 갈 수 없는 경우
        if turn_time == 4:
            ny = y - dy[direction]
            nx = x - dx[direction]
            # 뒤로 갈 수 있다면 이동하기
            if maps[ny][nx] == 0:
                y, x = ny, nx
            else:
                break
            turn_time = 0
    return count


n1, m1 = 4, 4
avatar1 = [1, 1, 0]
map1 = [[1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1]]

print(solution(n1, m1, avatar1, map1))
