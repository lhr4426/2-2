# 2번 정답

arr = [4, 7, 9, 1, 3, 5, 2, 3, 4]

count = [0] * (max(arr) + 1)

for num in arr :
  count[num] += 1

for i in range(1, len(count)) :
  count[i] += count[i-1]
  
result = [0] * (len(arr))

for num in arr :
  idx = count[num]
  result[idx - 1] = num
  count[num] -= 1
print(result)