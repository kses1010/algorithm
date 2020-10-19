# 1934

test_count = int(input())
lcm_list = []
for i in range(0, test_count):
    input_number = input().split()
    a = int(input_number[0])
    b = int(input_number[1])

    std_number = a
    gcd, lcm = 1, 1
    if a < b:
        std_number = b

    if a == 0 or b == 0:
        gcd, lcm = 0, 0
    else:
        for j in range(1, std_number + 1):
            if a % j == 0 and b % j == 0:
                gcd = j
        if gcd != 1:
            lcm = gcd * (a // gcd) * (b // gcd)
        else:
            lcm = a * b
    lcm_list.append(lcm)

for k in range(len(lcm_list)):
    print(lcm_list[k])
