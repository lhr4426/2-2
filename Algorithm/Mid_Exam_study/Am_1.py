# 백준 1966번
# 문제 : 8개 정수 있을 때 가장 큰 정수 5개 합이랑 몇 번째인지

items = [int(input()) for _ in range(8)]
idx = []

for i in range(5) :
    max_idx = items.index(max(items))
    idx.append(max_idx)
    
    

