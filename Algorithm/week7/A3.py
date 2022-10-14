# 3번 정답

score = [int(input()) for _ in range(8)]

sum = 0
idx = []

for i in range(5):
  sum += max(score)
  a = score.index(max(score))
  idx.append(str(a + 1))
  score[a] = 0

idx.sort()
print(sum)
print(' '.join(idx))
