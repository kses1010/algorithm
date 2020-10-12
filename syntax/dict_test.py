import collections

a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
print(a)
a['C'] += 1
print(a)

for i, k in enumerate(a):
    print(i, k, a[k])
    print("---")

b = [1, 2, 3, 4, 5, 5, 5, 6, 6]
c = collections.Counter(b)
print(c)
print(c.most_common(2))

d = collections.OrderedDict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2})
print(d)
