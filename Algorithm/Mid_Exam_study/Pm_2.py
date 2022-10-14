# 백준 2839번
# 문제 : 상근이의 설탕배달

kilo = int(input())
bags = 0

while kilo > 0 :
    if kilo % 5 == 0 :
        bags += 1
        kilo -= 5
    elif kilo % 3 == 0 :
        bags += 1
        kilo -= 3
    else :
        if kilo > 4 :
            bags += 1
            kilo -= 5
        elif kilo > 2 :
            bags += 1
            kilo -= 3
        else :
            print(-1)
            exit(1)

print(bags)
    
