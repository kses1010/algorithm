# 만들 수 없는 금액

def solution(money):
    money.sort()
    target = 1
    for i in money:
        # 만들 수 없는 금액을 찾았을 때 반복 종료
        if target < i:
            break
        target += i
    return target


arr1 = [3, 2, 1, 1, 9]
arr2 = [3, 5, 7]
arr3 = [1, 2, 3]
print(solution(arr1))
print(solution(arr2))
print(solution(arr3))
