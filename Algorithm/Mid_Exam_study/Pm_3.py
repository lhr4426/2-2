# 문제 : 하노이탑

def hanoi(items, start, end, notUse) :
    if items == 1 :
        print(start, end)
        return
    
    hanoi(items-1, start, notUse, end) # 제일 큰 거 제외 나머지를 보조로 옮기기
    print(start, end) # 제일 큰 거를 끝으로 옮기기
    hanoi(items-1, notUse, end, start) # 보조에 있던 걸 끝으로 옮기기

    return

# items = int(input())

items = 3

print(2 ** items - 1)
hanoi(items, 1, 3, 2)