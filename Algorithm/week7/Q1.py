# 문제 : 힙정렬 오름차순

def heap_sort(item):
  newlist = []
  build_max_heap(items)
  for i in range(len(items) - 1, 0, -1):
    items[1], items[i] = items[i], items[1]
    # 남은 힙에서 가장 큰 값이 i 위치로 이동하게 됨
    newlist.insert(0, items.pop(i))
    # 새로운 리스트에 기존 힙의 i 위치에 있는 값을 추가함과 동시에 기존에서는 뺌
    max_heapify(items, 1)
    # 변경된 힙을 다시 max heap으로 변경함
  return newlist


def build_max_heap(items):
  if items[0] != 0:
    items.insert(0, 0)
  maxIndex = items.index(max(items))
  items[1], items[maxIndex] = items[maxIndex], items[1]
  heapSize = len(items) - 1
  for i in range(heapSize // 2, 1, -1):
    max_heapify(items, i)

  return items


def max_heapify(items, nodeIndex):
  if len(items) - 1 < nodeIndex * 2 + 1:
    return

  if items[nodeIndex * 2] > items[nodeIndex * 2 + 1]:
    maxChildIndex = nodeIndex * 2
  else:
    maxChildIndex = nodeIndex * 2 + 1

  if items[nodeIndex] >= items[maxChildIndex]:
    return

  items[nodeIndex], items[maxChildIndex] = items[maxChildIndex], items[
    nodeIndex]
  max_heapify(items, maxChildIndex)


items = [5, 7, 2, 9, 2, 5, 6, 9, 10, 36]
print("초기 값 : ", items)

sorteditems = heap_sort(items)
print("힙 정렬 후 값 : ", sorteditems)
