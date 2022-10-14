#### 알고리즘 5주차

##### 재귀 : 자기 자신을 호출하는 함수

구성 : Base case(Termination condition) 1개 이상, Recursive case  

- - -

##### 분할정복 : 하위 문제로 나눠서 재귀적으로 해결하고 합침

분할 : 한 문제를 유형이 비슷한 여러 개의 하위 문제로 나눔  
정복 : 재귀적으로 해결  
병합 : 합쳐서 원래 문제를 해결  

- - -

##### 병합 정렬 : 반씩 쪼개서 병합함

원리 : 원소가 1개가 남을 때 까지 나누고 이를 순서에 맞춰 다시 합침  
균등 분할 방식(위치 기준 분할)  
입력 구성에 따른 차이가 없음  

```python
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

```
