# 문제 : 소수 판별

input_num = int(input())

for i in range(2, input_num):
  if input_num % i == 0 :
    print("{}는 {}로 나누어지기 때문에 소수가 아닙니다.".format(input_num, i))
    break
  else :
    if i == input_num - 1 :
      print("{}는 소수입니다.".format(input_num))