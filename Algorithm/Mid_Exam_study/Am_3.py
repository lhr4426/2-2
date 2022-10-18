# 백준 5568번
# 문제 : n장에서 k장 선택해서 만들 수 있는 수 개수

from itertools import permutations as p

n = int(input())
k = int(input())

items = [str(input()) for _ in range(n)]
nPk = list(p(items, k))
newitems = list(set([int(''.join(s for s in nPk[i])) for i in range(len(nPk))]))

print(len(newitems))
