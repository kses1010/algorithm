a = [1, 2, 3, 2, 45, 2, 5]
print(list(enumerate(a)))

b = ['a1', 'b2', 'c3']
for i in range(len(b)):
    print(i, b[i])
print('---------')

j = 0
for v in b:
    print(j, v)
    j += 1
print('---------enumerate')

for i, v in enumerate(b):
    print(i, v)

for i in enumerate(b):
    print(i)


print("------------")
users = []

if not users:
    print('no users')

