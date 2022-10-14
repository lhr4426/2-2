# 문제 : 10개 역순 출력 / 최대값과 그 인덱스 출력

number_list = list(map(int, input().split()))
number_len = len(number_list)

for i in range(number_len):
  print(number_list[number_len -1 - i], end = ' ')
print()

max_index = 0

for i in range(number_len):
  if number_list[max_index] < number_list[i] :
    max_index = i

print("최댓값 : {0}, 인덱스 : {1}".format(number_list[max_index], max_index))