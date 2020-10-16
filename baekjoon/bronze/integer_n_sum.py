def solve(a: list) -> int:
    ans = 0
    for i in a:
        ans += i

    return ans


list_a = [1, 2, 3]
print(solve(list_a))
