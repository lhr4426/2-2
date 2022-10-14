# 문제 : 별찍기

for i in range(5):
  star_count = i * 2 + 1
  blank_count = int((9 - star_count) / 2)
  print(" " * blank_count, end='')
  print("*" * star_count, end='')
  print(" " * blank_count)

for i in range(5) :
  star_count = 9 - (i * 2)
  blank_count = i
  print(" " * blank_count, end='')
  print("*" * star_count, end='')
  print(" " * blank_count)
