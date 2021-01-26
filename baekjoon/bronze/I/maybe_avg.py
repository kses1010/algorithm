# 4344 - 평균은 넘겠지
from sys import stdin

inputs = stdin.readline

n = int(inputs())
answer = []


def calculate_avg(scores):
    student_count = scores[0]
    scores_avg = (sum(scores[1:]) / student_count)
    count = 0
    for s in scores[1:]:
        if s - scores_avg > 0:
            count += 1
    ratio = (count / student_count) * 100
    return ratio


for i in range(n):
    score_list = list(map(int, inputs().split()))
    answer.append(calculate_avg(score_list))

for i in answer:
    print(f'{i:.3f}%')
