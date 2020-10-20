# 9613

from itertools import combinations
from math import gcd

count = int(input())
gcd_list = []
for i in range(count):
    number_list = list(map(int, input().split()))
    gcd_sum = 0
    number_list = number_list[1:]
    for a, b in combinations(number_list, 2):
        gcd_sum += gcd(a, b)

    gcd_list.append(gcd_sum)

for j in range(len(gcd_list)):
    print(gcd_list[j])
