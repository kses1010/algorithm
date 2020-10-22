# 시간 초과
# def solution(participant: [str], completion: [str]) -> str:
#     for i in range(len(completion)):
#         if completion[i] in participant:
#             participant.remove(completion[i])
#
#     if not participant:
#         return ''
#
#     answer = participant.pop()
#     return answer
import collections


def solution(participant: [str], completion: [str]) -> str:
    answer = ''
    parti_dict = collections.defaultdict(int)
    for i in range(len(participant)):
        parti_dict[participant[i]] += 1

    for i in range(len(completion)):
        parti_dict[completion[i]] -= 1

    for k, v in parti_dict.items():
        if v == 1:
            answer = k

    return answer


participant1 = ['leo', 'kiki', 'eden']
completion1 = ['eden', 'kiki']
participant2 = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion2 = ['josipa', 'filipa', 'marina', 'nikola']
participant3 = ['mislav', 'stanko', 'mislav', 'ana']
completion3 = ['stanko', 'ana', 'mislav']

print(solution(participant1, completion1))
print(solution(participant2, completion2))
print(solution(participant3, completion3))
