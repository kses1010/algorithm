a = ['cde', 'cfc', 'abc']


def fn(s):
    return s[0], s[-1]


list_a = sorted(a, key=lambda s: (s[0], s[-1]))

print(list_a)
print(sorted(a, key=fn))
