# 문제 : 우선순위 프린터

caseCount = int(input())

result = []

for i in range(caseCount) :
  n, m = list(map(int, input().split()))
  oldItems = list(map(int, input().split()))
  newItems = sorted(oldItems, reverse=True)
  result.append([newItems.index(oldItems[m])+1])

print(result)