# 2164 카드2
from collections import deque

n = int(input())
card = [i + 1 for i in range(n)]
card_deck = deque(card)

while len(card_deck) > 1:
    card_deck.popleft()
    num = card_deck.popleft()
    card_deck.append(num)

print(card_deck[0])
