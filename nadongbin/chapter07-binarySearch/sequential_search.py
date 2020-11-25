# 순차 탐색

def sequential_search(n, target, arr):
    # 각 원소를 하나씩 확인
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if arr[i] == target:
            # 현재의 위치 반환(인덱스가 0부터 시작하므로 1더하기)
            return i + 1


input_data = input().split()
n1 = int(input_data[0])
target1 = input_data[1]
print("===")
arr1 = input().split()

print(sequential_search(n1, target1, arr1))
