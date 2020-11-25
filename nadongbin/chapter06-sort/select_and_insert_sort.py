# 선택 정렬
arr1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(arr1)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(arr1)):
        if arr1[min_index] > arr1[j]:
            min_index = j
    arr1[i], arr1[min_index] = arr1[min_index], arr1[i]  # 스왑

print(arr1)

# 삽입 정렬
arr2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(arr2)):
    # 인덱스 i 부터 1까지 감소하며 반복한다.
    for j in range(i, 0, -1):
        # 한 칸씩 왼쪽으로 이동
        if arr2[j] < arr2[j - 1]:
            arr2[j], arr2[j - 1] = arr2[j - 1], arr2[j]
        # 자기보다 작은 데이터를 만나면 그 위치에서 멈추기
        else:
            break
print(arr2)

