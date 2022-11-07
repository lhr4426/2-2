from collections import deque

def bfs(start): # 너비 우선 탐색
  count = 0 # 1번 자신은 세지 않음
  queue = deque([start]) # 큐 사용
  visited[start] = True # 시작지점 방문처리
  while queue:
    n = queue.popleft() 

    for i in graph[n]: 
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        count = count + 1
  return count


n = int(input())
m = int(input())

graph = [[] for _ in range(n)] 

for i in range(m):
  a, b = map(int, input().split()) 
  graph[a - 1].append(b - 1) # 입력이 1에서부터 들어오기 때문에 1을 빼야함 
  graph[b - 1].append(a - 1)
for i in range(n):
  graph[i].sort()

visited = [False] * (n) # 방문처리를 위한 배열

count = bfs(0)

print(count)
