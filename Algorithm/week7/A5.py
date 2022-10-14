# 5번 정답

from itertools import permutations as p

n = int(input())
k = int(input())
num = [str(input()) for _ in range(n)]

print(len(set(list(''.join(i) for i in p(num,k)))))