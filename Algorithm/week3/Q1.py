# 문제 : reverse() 쓰지말고 반대로 출력

def desc(item):
    item = str(item)
    item_len = len(item)
    new_item = ""
    for i in range(item_len):
        new_item += item[item_len - 1 - i]
    new_item = int(new_item)

    return new_item


n = int(input())
print(desc(n))