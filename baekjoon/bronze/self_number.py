nums = set(range(1, 10001))
args_nums = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    args_nums.add(i)

self_number = nums - args_nums

for i in sorted(self_number):
    print(i)
