# 문제 : 정수를 이어붙여 만들 수 있는 가장 큰 수 출력

import itertools

ITEMCOUNT_ = 5

def mergeSort(items):
  if len(items) <= 1:
    return items

  mid = len(items) // 2
  leftitems = items[:mid]
  rightitems = items[mid:]
  leftside = mergeSort(leftitems)
  rightside = mergeSort(rightitems)
  return merge(leftside, rightside)


def merge(leftside, rightside):
  sortedList = []
  i = 0
  j = 0

  while (i < len(leftside)) and j < len(rightside):
    if leftside[i] > rightside[j]:
      sortedList.append(leftside[i])
      i += 1
    else:
      sortedList.append(rightside[j])
      j += 1

  while (i < len(leftside)):
    sortedList.append(leftside[i])
    i += 1
  while (j < len(rightside)):
    sortedList.append(rightside[j])
    j += 1

  return sortedList


items = [3, 30, 34, 5, 9]
permu = list(itertools.permutations(items, ITEMCOUNT_))
strings = []

for i in range(len(permu)):
  a, b, c, d, e = permu[i]
  itemstr = '' + str(a) + str(b) + str(c) + str(d) + str(e)
  strings.append(int(itemstr))

print(mergeSort(strings)[0])
