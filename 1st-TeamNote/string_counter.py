import collections


def solution(s):
    str_counter = collections.Counter(s)
    str_list = sorted(str_counter.items(), key=lambda x: (-x[1], x[0]))
    return str_list


print(solution('aabccdeff'))
