# 문제 : 주어진 완전 이진 트리가 Max-Heap 인지 확인

def isMaxHeap(items, i) :
  if len(items) - 1 < 2*i + 1 : # len(items)는 0도 포함하기 때문에 1 뺌
    return
  if items[i] > items[2*i] and items[i] > items[2*i + 1] :
    isMaxHeap(items, i+1)
  else :
    return False

items = [0] # max heap은 리스트 인덱스로 0을 사용하지 않아서 미리 채워둠
inputitems = list(map(int, input().split()))
items += inputitems

if isMaxHeap(items, 1) == False :
  print("items is not max heap")
else :
  print("items is max heap")
