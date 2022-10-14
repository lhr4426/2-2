# 문제 : 뽑은 카드 3장 숫자 더해서 만들 수 있는 모든 숫자의 개수 출력

import random

card_count, max_count = map(int, input().split())
card_list = []
result_list = []

for i in range(card_count):
    card_list.append(random.randint(1, 100))

for i in range(card_count - 2):
    for j in range(card_count - 1):
        for k in range(card_count):
            result_list.append(card_list[i] + card_list[j] + card_list[k])

result_list = list(set(result_list))
result_list.sort(reverse=True)

print(result_list[max_count - 1])
