# 문제 : 숫자 카드 비교 회수 출력

import math

def makeMaxHeap(items):
  if items[0] != 0 :
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
  

inputs = [10, 20, 40]

print("초기 값 : {}".format(inputs))

sorteditem = makeMaxHeap(inputs)
print("정렬 후 : {}".format(sorteditem))

depth = math.trunc(math.log2(len(sorteditem)-1))
print(depth)

doublePlus = []
doublePlus.append(sorteditem[depth*2] + sorteditem[depth*2+1])
doublePlus.append(sorteditem[1] + doublePlus[-1])
doublePlus.append(doublePlus[-1] + doublePlus[0])

sorteditem += doublePlus
print (makeMaxHeap(sorteditem))

print(sorteditem[1])

