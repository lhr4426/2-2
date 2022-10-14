#### 알고리즘 6주차

##### 퀵정렬 : 피벗 기준으로 나눠서 피벗 위치를 확정해 감

비균등 분할 방식(값에 따른 분할)  
오름차순 기준으로,  
피벗보다 작은 수들은 피벗의 앞에, 피벗보다 큰 수들은 피벗의 뒤에 위치하게 한다.  
이미 정렬된 리스트를 퀵정렬로 다시 정렬하면 시간 복잡도가 O(n<sup>2</sup>)까지 커진다.  
이를 보완하기 위한 Randomized Quick Sort도 존재한다.  
이는 피벗을 랜덤하게 설정하고 퀵정렬을 진행하는 방법이다.  

```python
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
```

- - -

##### 힙정렬 : 힙으로 만들어서 정렬한다

완전 이진 트리 : 마지막 레벨 제외, 모든 레벨이 완전히 채워져 있으며 마지막 레벨은 왼쪽에서 오른쪽으로 채워져 있어야 함  
힙은 완전 이진 트리의 일종이며, 반정렬 상태를 유지한다.  
같은 값으로 힙을 만들어도 만들어진 힙이 다를 수도 있다.  
배열을 통해 힙을 만들 때는 0번째 자리는 사용하지 않는다.  

루트노드 : A[1]  
A[i]의 부모 : A[i//2]  
A[i]의 왼쪽 자식 : A[2i]  
A[i]의 오른쪽 자식 : A[2i + 1]  