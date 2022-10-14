# 문제 : 숫자카드 문제

def selectionSort(item_list):
    for last in range(len(item_list) - 1, 0, -1):
        max_index = 0
        for i in range(last + 1):
            if item_list[max_index] < item_list[i]:
                max_index = i
        item_list[max_index], item_list[last] = item_list[last], item_list[
            max_index]

    return item_list


def findItem(item_list, find_num):
    count = 0

    for i in range(len(item_list)):
        if item_list[i] == find_num:
            count += 1

    return count


N_count = int(input())
N_list = list(map(int, input().split()))
M_count = int(input())
M_list = list(map(int, input().split()))

counting_list = []

selectionSort(N_list)

for i in range(M_count):
    counting_list.append(findItem(N_list, M_list[i]))

print(counting_list)
