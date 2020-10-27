# 1475
import math

room_num = list(map(int, str(input())))
num_set = [0] * 9
for i in room_num:
    if i == 6 or i == 9:
        num_set[5] += 0.5
    else:
        num_set[i] += 1

print(math.ceil(max(num_set)))
