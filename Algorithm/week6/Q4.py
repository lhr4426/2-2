# 문제 : Max-heapify 알고리즘 직접 구현

def makeMaxHeap(items):
  items.insert(0, 0)
  maxindex = items.index(max(items))
  items[1], items[maxindex] = items[maxindex], items[1]
  heapSize = len(items) - 1
  for i in range(heapSize // 2, 0, -1) :
    maxHeapfify(items, i)

  return items


def maxHeapfify(items, i):
  if len(items) - 1 < 2*i + 1 :
    return
    
  k = 0
  
  if items[2*i] > items[2*i+1] :
    k = 2 * i
  else :
    k = 2 * i + 1

  if items[i] >= items[k] :
    return

  items[i], items[k] = items[k], items[i]
  maxHeapfify(items, k)
  

inputs = [4, 16, 15, 8, 7, 13, 14, 2, 5]

print("초기 값 : {}".format(inputs))

sorteditem = makeMaxHeap(inputs)
print("정렬 후 : {}".format(sorteditem))