# 문제 : A[i] + ... + A[j] 가 M이 되는 경우의 수

item_setting = list(map(int, input().split()))
item_list = list(map(int, input().split()))
count = 0

for i in range(item_setting[0]):

    for j in range(i, item_setting[0]):

        if sum(item_list[i:j+1]) == item_setting[1]:
            print(item_list[i:j+1])
            count += 1

print(count)
