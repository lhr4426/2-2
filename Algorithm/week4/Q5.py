# 문제 : 좌표압축

def selectionSort(item_list):
    for last in range(len(item_list) - 1, 0, -1):
        max_index = 0
        for i in range(last + 1):
            if item_list[max_index] < item_list[i]:
                max_index = i
        item_list[max_index], item_list[last] = item_list[last], item_list[
            max_index]

    return item_list


N_count = int(input())
N_list = list(map(int, input().split()))
N_list2 = []

for i in range(N_count):
    N_list2.append(N_list[i])

N_list2 = list(set(N_list2))

sortedlist = selectionSort(N_list2)

dictitem = {numbers: i for i, numbers in enumerate(sortedlist)}

answer = []

for i in range(N_count):
    answer.append(dictitem.get(N_list[i]))

print(answer)
