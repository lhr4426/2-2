#### 알고리즘 7주차

##### 힙정렬 : 힙으로 만들어서 정렬한다

max-heapify : 자식 노드가 있는 부모 노드 대상으로, 둘 중 더 큰 자식 노드와 부모노드를 비교해 큰 노드가 부모 노드가 됨  
build-max-heap : 0번째 자리 0으로 두고, 배열 크기의 반절에서부터 max-heapify 반복해서 1번째 자리까지 함  
힙정렬 : 1번째 자리 애랑 i번째 자리 애랑 바꿈 (이때 i는 맨 마지막부터 2까지 돎)  

```python
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
```

- - -

##### 계수 정렬 : 사전지식을 이용함

비교하지 않는 정렬  
그냥 몇 번 나오나 세서 그걸로 다시 배열 만들면 됨  

```python
base_list = [i for i in range(1, 6)]
# 예시는 1에서 5까지만 존재한다고 가정

test_list = [1, 5, 2, 4, 1, 2, 3, 1, 5, 2, 4, 1, 2, 5, 1, 4, 2, 1, 3, 2, 5]

print("초기 : ", test_list)

counting_dict = {base: 0 for base in base_list}
# value값이 0으로 초기화된 딕셔너리 생성

for item in test_list:
  counting_dict[item] += 1

print("딕셔너리 : ", counting_dict)

new_list = []

for i in range(1, 5):
  new_list += counting_dict[i] * [i]

print("결과 : ", new_list)
```
