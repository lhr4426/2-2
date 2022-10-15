# 백준 1966번
# 문제 : 우선순위 프린터 큐

def printerQueue(old_Q, first_Loc) :
    new_Q = range(len(old_Q)) # 0에서 n-1 까지 배열 만듬. 초기 인덱스 위치임

    result = [] # 하나씩 넣을 배열
    lastidx = 0 # 마지막 인덱스

    while len(result) < len(old_Q) :
        maxold = max(old_Q) # input 값중에 가장 큰거
        maxidx = old_Q.index(maxold) # maxold 위치

        if lastidx > len(old_Q) - 1 : # lastidx가 범위 넘어가면 다시 0으로 조정
            lastidx = 0

        if old_Q.count(maxold) == 1 : # 큰 값이 중복 없이 하나만 존재하면
            result.append(new_Q[maxidx]) # 가장 큰 값이 들어온 순번을 result에 넣음
            old_Q[maxidx] = 0 # max에 안잡히게 0으로 만듬
            lastidx = maxidx + 1 # 마지막 인덱스는 maxidx의 다음
        else : # 중복 있으면?
            result.append(new_Q[lastidx]) # lastidx 위치에 있는 순번을 result에 넣음 
            old_Q[lastidx] = 0 # max에 안잡히게 0으로 만듬
            lastidx += 1 # lastidx 하나 증가

    return result.index(first_Loc) + 1

case_count = int(input())
results = []

for i in range(case_count) :
    n, m = list(map(int, input().split()))
    priority = list(map(int, input().split()))
    results.append(printerQueue(priority, m))

for i in range(case_count) :
    print(results[i])



