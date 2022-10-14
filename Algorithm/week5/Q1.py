# 문제 : 병합 정렬 구현

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
    if leftside[i] < rightside[j]:
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


test_list = [1, 9, 4, 0, 27, 945, 12, 96, 990, 231, 592]
print(test_list)
print(mergeSort(test_list))
