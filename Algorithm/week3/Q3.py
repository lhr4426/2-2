# 문제 : 달팽이 올라가기

item_list = list(map(int, input().split()))
days = 0
up_dalpang = 0

while up_dalpang < item_list[2]:
    days += 1

    up_dalpang += item_list[0]
    if up_dalpang == item_list[2]:
        break

    up_dalpang -= item_list[1]

print(days)
