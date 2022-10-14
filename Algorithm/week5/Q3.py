# 문제 : 배열 자르고 정렬해서 k번째에 있는 수 구하기

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


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
result = []

for x in range(0, 3):
  i, j, k = commands[x]
  testing = array[i - 1:j]
  testing_ = mergeSort(testing)
  result.append(testing_[k - 1])

print(result)
