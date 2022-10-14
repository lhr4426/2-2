# 4번 정답

t = int(input())

result = []
for i in range(t):
  n, m = map(int, input().split())
  Q = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]

  cnt = 0
  while True:
    cur = Q.pop(0)
    if any(cur[1] < x[1] for x in Q):
      Q.append(cur)
    else:
      cnt += 1
      if cur[0] == m:
        result.append(cnt)
        break
for i in result:
  print(i)