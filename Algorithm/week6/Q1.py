# 문제 : 퀵정렬 오름차순 구현

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


itemsList = [1, 5, 2, 7, 4, 4, 8, 3]
print(itemsList)
quickSort(itemsList, 0, len(itemsList) - 1)
print(itemsList)
