# 2609

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
    for i in range(1, std_number + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    if gcd != 1:
        lcm = gcd * (a // gcd) * (b // gcd)
    else:
        lcm = a * b

print(gcd, lcm)
