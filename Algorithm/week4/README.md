#### 알고리즘 4주차

##### 정렬 : 특정 조건에 맞춰 재배열하는 것

하는 이유 : 탐색 용이함  
시간 복잡도 :  
	선택, 버블, 삽입 = O(n<sup>2</sup>)  
	병합, 퀵, 힙 = O(nlogn)  
	카운팅 = O(n)  
- - -

##### 선택 정렬 : 매 순간 특정 숫자(최대or최소)를 선택해서 맨 끝으로 보냄

제자리 정렬 알고리즘(추가메모리 요구 x)  
자료 이동 회수가 미리 결정됨  
입력에 민감하지 않은 알고리즘  

Outer-loop 한 번 당 원소 하나의 최종위치 결정됨  

```python
def selectionSort(item_list):
    for last in range(len(item_list) - 1, 0, -1):
        max_index = 0
        for i in range(last + 1):
            if item_list[max_index] < item_list[i]:
                max_index = i
        print(item_list[max_index])
        item_list[max_index], item_list[last] = item_list[last], item_list[
            max_index]
        print(item_list)
```

- - -

##### 버블 정렬 : 매 순간 인접 숫자와 비교해서 특정 숫자를 이동시킴

구현 매우 쉬움  
교환이 많음  

```python
def bubbleSort(item_list):
    for last in range(len(item_list) - 1, 0, -1):
        for i in range(last):
            if item_list[i] > item_list[i + 1]:
                item_list[i], item_list[i + 1] = item_list[i + 1], item_list[i]
        print(item_list)
```

- - -

##### 삽입 정렬 : 정렬된 배열을 점점 증가시킴

정렬 된 부분(앞부분)에다가 정렬 안 된 부분(뒷부분)의 원소를 하나씩 자리에 맞게 끼움  
입력에 민감함!  

```python
def insertionSort(item_list):
    for change in range(1, len(item_list)):
        sortindex = change - 1
        tmp = item_list[change]
        print(tmp, change)

        while sortindex >= 0 and tmp < item_list[sortindex]:
            item_list[sortindex + 1], item_list[sortindex] = item_list[
                sortindex], item_list[sortindex + 1]
            sortindex -= 1

        item_list[sortindex + 1] = tmp

        print(item_list)
```


