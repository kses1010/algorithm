import copy

a = [1, 2, 3]
b = a
c = a[:]
print(id(a))
print(id(b))
print(id(c))
print("==============")

d = a.copy()
print(id(a))
print("-------------")

ab = [1, 2, [3, 5], 4]
ba = copy.deepcopy(ab)
print(id(ab))
print(id(ba))
print(ba)
