# 문제 : 올바른 스도쿠 확인

row_col = int(input())

num_list = list(range(1, row_col + 1))
testing_sum = sum(num_list)
sqrt_rowcol = int(row_col**(1 / 2))

input_list = []

for i in range(row_col):
    tmp_row = list(map(int, input().split()))
    input_list.append(tmp_row)

isGoodSudoku = True
col_sum = 0

for i in range(row_col):
    if sum(input_list[i]) != testing_sum:
        isGoodSudoku = False
    for j in range(row_col):
        col_sum += input_list[j][i]

    if col_sum != testing_sum:
        isGoodSudoku = False

    col_sum = 0

nemo_sum = [[0]*sqrt_rowcol for _ in range(sqrt_rowcol) ]

for i in range(row_col) :
  for j in range(row_col) :
    nemo_sum[i // sqrt_rowcol][j // sqrt_rowcol] += input_list[i][j]

for i in range(sqrt_rowcol) :
  for j in range(sqrt_rowcol) :
    if nemo_sum[i][j] != testing_sum :
      isGoodSudoku = False


if isGoodSudoku :
  print("YES")
else :
  print("NO")
    
  
  
