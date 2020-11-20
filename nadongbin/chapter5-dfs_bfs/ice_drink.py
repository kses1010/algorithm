# 음료수 얼려 먹기

def solution(arr):
    # DFS 로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
    def dfs(x, y):
        # 주어진 범위를 벗어나는 경우에는 즉시 종료
        if x <= -1 or x >= len(arr) or y <= -1 or y >= len(arr[0]):
            return False
        # 현재 노드를 아직 방문하지 않았다면
        if arr[x][y] == 0:
            # 해당 노드 방문 처리
            arr[x][y] = 1
            # 상, 하, 좌, 우 위치도 모두 재귀적으로 호출
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
        return False

    # 모든 노드(위치)에 대하여 음료수 채우기
    result = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            # 현재 위치에서 DFS 수행
            if dfs(i, j):
                result += 1
    return result


arr1 = [[0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]]

print(solution(arr1))
