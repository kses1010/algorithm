# 프린터
from collections import deque


def solution(priorities, location):
    # 인쇄물 요청 우선순위 포함 덱 만들기
    print_list = deque([(v, i) for i, v in enumerate(priorities)])
    priority = 0

    while print_list:
        # 가장 앞에 있는 문서
        j = print_list.popleft()

        # 최고값 비교해서 작으면 맨 뒤로
        if print_list and max(print_list)[0] > j[0]:
            print_list.append(j)
        # 크거나 같다면 우선순위 체크하고 원하는 문서이면 break
        else:
            priority += 1
            if j[1] == location:
                break
    return priority


priorities1, location1 = [2, 1, 3, 2], 2
priorities2, location2 = [1, 1, 9, 1, 1, 1], 0
print(solution(priorities1, location1))
print(solution(priorities2, location2))
