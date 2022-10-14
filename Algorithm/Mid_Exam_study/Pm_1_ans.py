# 1번 답

def finding_numbers(base_items, find_num) :
    start = 0
    mid = len(base_items) // 2
    end = len(base_items) - 1

    while start <= end :
        if find_num == base_items[mid] :
            return 1
        elif find_num > base_items[mid] :
            start = mid + 1
        else :
            end = mid - 1
        
        mid = start + (end - start) // 2
    
    return 0

base_count = 5
base_items = [4, 1, 5, 2, 3]
find_count = 5
find_items = [1, 3, 7, 9, 5]

base_items.sort()

for i in range(find_count) :
    print(finding_numbers(base_items, find_items[i]))