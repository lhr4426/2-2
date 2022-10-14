# 문제 : 0~100 사이 난수 50개 생성 후 동일 값 존재 유무 확인

import random

number_list = []

for i in range(50):
  number_list.append(random.randint(0,100))

print(number_list)

for i in range(50):
  for j in range(i + 1, 50):
    if number_list[i] == number_list[j]:
      print("{} 라는 숫자가 동일하게 존재합니다.".format(number_list[i]))

