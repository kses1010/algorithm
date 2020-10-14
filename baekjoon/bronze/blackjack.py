from itertools import combinations


def blackjack1() -> int:
    count, target_number = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    result = 0

    for i in range(count):
        for j in range(i + 1, count):
            for k in range(j + 1, count):
                if arr[i] + arr[j] + arr[k] > target_number:
                    continue
                else:
                    result = max(result, arr[i] + arr[j] + arr[k])
    return result


def blackjack2() -> int:
    count, target_number = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    result = 0

    for i in combinations(arr, 3):
        temp_sum = sum(i)
        if result < temp_sum <= target_number:
            result = temp_sum
    return result


print(blackjack1())
print(blackjack2())
