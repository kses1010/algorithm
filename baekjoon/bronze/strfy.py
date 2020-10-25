# 11328

input_number = int(input())

for i in range(input_number):
    input_str = input().split()
    a, b = input_str[0], input_str[1]
    if len(a) != len(b):
        print("Impossible")
    else:
        a = ''.join(sorted(a))
        b = ''.join(sorted(b))
        if a == b:
            print("Possible")
        else:
            print("Impossible")
