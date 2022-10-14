# 문제 : n장 카드 중 k장으로 만들 수 있는 정수 개수

import itertools

n = int(input())
k = int(input())
items = []

for i in range(n) :
  items.append(int(input()))

# 일단 모든 순열 구해보기
nPk = list(itertools.permutations(items, k))

# 문자열 -> 숫자로 변환해서 넣을 빈 배열 생성
changednPk = []

for i in range(len(nPk)):
  temp = ""
  for j in range(k) :
    # 일단 문자열로 바꾼걸 합침
    temp += str(nPk[i][j])

  # 그런 다음 문자열을 다시 숫자로 바꿔서 새 배열에 넣음
  changednPk.append(int(temp))

# 중복 제거를 위해 set을 사용
changednPk = list(set(changednPk))

print(changednPk)
print(len(changednPk))