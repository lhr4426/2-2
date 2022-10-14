# 문제 : 가장 평균에 가까운 학생 몇 번째인지

people_count = int(input())
people_score = list(map(int, input().split()))

sum_score = 0
avg_score = 0

for i in range(people_count) :
  sum_score += people_score[i]

avg_score = round(sum_score / people_count)

diff = avg_score - people_score[0]
diff_index = 0

for i in range(1, people_count) :
  if abs(diff) > abs(avg_score - people_score[i]) :
    diff_index = i
    diff = avg_score - people_score[i]
  elif abs(diff) == abs(avg_score - people_score[i]) :
    if people_score[diff_index] < people_score[i] :
      diff_index = i
      diff = avg_score - people_score[i]
    elif people_score[diff_index] == people_score[i] :
      if diff_index > i :
        diff_index = i

print(avg_score, end=' ')
print(diff_index + 1)