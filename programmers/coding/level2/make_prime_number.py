# 소수 만들기
from itertools import combinations


def solution(nums):
    count = 0

    def check_prime_number(num):
        if num < 2:
            return False
        m = int(num ** 0.5)
        for i in range(2, m + 1):
            if num % i == 0:
                return False
        return True

    list_num = list(combinations(nums, 3))
    list_sum = [sum(i) for i in list_num]

    for i in list_sum:
        if check_prime_number(i):
            count += 1
    return count


nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 7, 6, 4]
print(solution(nums1))
print(solution(nums2))
