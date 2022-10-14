# 문제 : 두 배열을 합친 후 정렬해서 출력

def quickSort(items, start, end):
  if start == end:
    return items

  if start < end:
    pivot = partition(items, start, end)
    quickSort(items, start, pivot - 1)
    quickSort(items, pivot, end)


def partition(items, start, end):
  lastItem = items[end]
  i = start - 1  # 피벗보다 작은 가장 마지막 위치 i
  for j in range(start, end):  # 탐색 위치 j
    if items[j] <= lastItem:
      i += 1
      items[i], items[j] = items[j], items[i]
  items[i + 1], items[end] = items[end], items[i + 1]
  return i + 1


itemConfig = list(map(int, input().split()))
allItems = []

for i in range(2):
  temp = list(map(int,input().split()))
  allItems += temp

print("원본 : {}".format(allItems))
quickSort(allItems, 0, len(allItems)-1)
print("정렬 후 : {}".format(allItems))
