# 문제 : 계수정렬 오름차순

base_list = [i for i in range(1, 6)]
# 예시는 1에서 5까지만 존재한다고 가정

test_list = [1, 5, 2, 4, 1, 2, 3, 1, 5, 2, 4, 1, 2, 5, 1, 4, 2, 1, 3, 2, 5]

print("초기 : ", test_list)

counting_dict = {base: 0 for base in base_list}
# value값이 0으로 초기화된 딕셔너리 생성

for item in test_list:
  counting_dict[item] += 1

print("딕셔너리 : ", counting_dict)

new_list = []

for i in range(1, 5):
  new_list += counting_dict[i] * [i]

print("결과 : ", new_list)
