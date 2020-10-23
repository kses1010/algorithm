# 10093

n1, n2 = map(int, input().split())

a = min(n1, n2)
b = max(n1, n2)

if a == b or a + 1 == b:
    print(0)
else:
    print(b - a - 1)

for i in range(a + 1, b):
    print(i, end=' ')
