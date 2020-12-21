# 카드 정렬하기
import heapq
from sys import stdin

inputs = stdin.readline

num = int(inputs())

cards = [int(inputs()) for _ in range(num)]

# 시간초과
cards.sort()
count = 0

if len(cards) < 3:
    print(sum(cards))

sum_list = [cards[0] + cards[1]]
for i in range(2, len(cards)):
    sum_list.append(sum(sum_list) + cards[i])

print(sum(sum_list))


# 우선순위 큐
def solution(card_list):
    heap = []
    for j in card_list:
        heapq.heappush(heap, j)
    result = 0

    # 힙에 원소가 1개 남을 때까지
    while len(heap) != 1:
        # 가장 작은 2개의 카드 묶음 꺼내기
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)
        # 카드 묶음을 합쳐 다시 삽입
        sum_card = one + two
        result += sum_card
        heapq.heappush(heap, sum_card)

    return result


print(solution(cards))
