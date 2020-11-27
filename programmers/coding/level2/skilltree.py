# 스킬 트리
import collections


def solution(skill, skill_trees):
    answer = 0
    skill_map = collections.OrderedDict()
    for i, v in enumerate(skill):
        skill_map[v] = int(i)
    for i in skill_trees:
        skill_list = []
        for s in i:
            if s in skill_map:
                skill_list.append(skill_map[s])
        check_list = [j for j in range(len(skill_list))]
        if check_list == skill_list:
            answer += 1
        skill_list.clear()

    return answer


skill1, skill_trees1 = "CBD", ["BACDE", "CBADF", "AECB", "BDA", "CED"]
print(solution(skill1, skill_trees1))
