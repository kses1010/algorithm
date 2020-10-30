import collections

a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5]
c = [3, 4, 5]
zip_test = list(zip(a, b))
zip_test2 = list(zip(a, b, c))
print(zip_test)
print(zip_test2)

a1 = ['a1', 'a2']
b1 = ['b1', 'b2']
c1 = ['c1', 'c2']
d1 = ['d1', 'd2']
print(list(zip(a1, b1, c1, d1)))

print("=============")
nums, k = [1, 1, 1, 2, 2, 3], 2
print(collections.Counter(nums).most_common(k))
print(list(zip(*collections.Counter(nums).most_common(k))))
print(list(zip(collections.Counter(nums).most_common(k))))

print("-------------")
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(*fruits)

print("---------------")
a2, *b2 = [1, 2, 3, 4]
print(a2)
print(b2)
*a2, b2 = [1, 2, 3, 4]
print(a2)
print(b2)

print("-=-=-=-=-=-=-=-=-=")
date_info = {'year': '2020', 'month': '10', 'day': '01'}
new_info = {**date_info, 'day': '31'}
print(new_info)
