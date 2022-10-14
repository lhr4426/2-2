# 문제 : N개 중 K번째 숫자 출력

def selectionSort(item_list):
    for last in range(len(item_list) - 1, 0, -1):
        max_index = 0
        for i in range(last + 1):
            if item_list[max_index] < item_list[i]:
                max_index = i
        item_list[max_index], item_list[last] = item_list[last], item_list[
            max_index]


n = list(map(int, input().split()))
k = list(map(int, input().split()))

selectionSort(k)

print(k[-n[1]])

