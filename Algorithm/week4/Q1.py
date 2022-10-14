# 문제 : 삽입, 선택, 버블 정렬을 오름차순으로 구현

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


def bubbleSort(item_list):
    for last in range(len(item_list) - 1, 0, -1):
        for i in range(last):
            if item_list[i] > item_list[i + 1]:
                item_list[i], item_list[i + 1] = item_list[i + 1], item_list[i]
        print(item_list)


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


input_data = [13, 25, 41, 62, 84, 11, 21]

insertionSort(input_data)
