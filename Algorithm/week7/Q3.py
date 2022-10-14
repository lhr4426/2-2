# 문제 : 가장 큰 정수 5개 합 / 몇 번째 정수

items = [20, 30, 50, 48, 33, 66, 0, 64]

sortedItems = sorted(items, reverse = True)

indexlist = []
result = 0

print(items)
print(sortedItems)

for i in range(5) :
  # 1. 기존 리스트에서 큰 순서대로 찾는다
  indexlist.append(items.index(sortedItems[i])+1)
  # 2. 상위 5개의 값을 점점 더한다
  result += sortedItems[i]

print(result)

indexlist = sorted(indexlist)

print(*indexlist)
