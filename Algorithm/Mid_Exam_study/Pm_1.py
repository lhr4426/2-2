# 백준 1920번
# 문제 : 이진탐색으로 정수 존재 확인

def find_number(items, i) :
    left = 0
    right = len(items) - 1
    mid = right // 2

    while len(items) > 1 :
        if i > items[mid] :
            left = mid + 1
        elif i < items[mid] :
            right = mid - 1
        else :
            return 1

        mid = (right - left) // 2
        items = items[left : right + 1]
    
    if i == items[0] :
        return 1
    else :
        return 0

# base_count = int(input())
# base_items = list(map(int, input().split()))
# find_count = int(input())
# find_items = list(map(int, input().split()))

base_count = 5
base_items = [4, 1, 5, 2, 3]
find_count = 5
find_items = [1, 3, 7, 9, 5]

base_items.sort()

for i in range(find_count) :
    print(find_number(base_items, find_items[i]))

    

