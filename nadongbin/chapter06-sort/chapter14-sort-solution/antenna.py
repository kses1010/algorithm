# 안테나

n = int(input())
house_list = list(map(int, input().split()))
house_list.sort()

print(house_list[(n - 1) // 2])
