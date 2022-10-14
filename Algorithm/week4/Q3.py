# 문제 : (x,y) 좌표를 y 우선 오름차순으로 정렬

def selectionSort(item_list):
    for last in range(len(item_list) - 1, 0, -1):
        max_index = 0
        for i in range(last + 1):
            if item_list[max_index][1] < item_list[i][1] or (
                    item_list[max_index][1] == item_list[i][1]
                    and item_list[max_index][0] < item_list[i][0]):
                max_index = i

        item_list[max_index], item_list[last] = item_list[last], item_list[
            max_index]

    print(item_list)


count = int(input())
pos_list = []

for i in range(count):
    pos_list.append(list(map(int, input().split())))

selectionSort(pos_list)
