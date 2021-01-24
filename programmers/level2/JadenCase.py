# JadenCase 문자열 만들기

def solution(s):
    word_list = s.split()
    answer_list = []
    for i in word_list:
        answer_list.append(i[0].upper() + i[1:].lower())

    return ' '.join(answer_list)


def solution2(s):
    return s.title()


s1 = "3people unFollowed me"
s2 = "for the last week"
print(solution(s1))
print(solution(s2))
print(solution2(s1))
print(solution2(s2))
