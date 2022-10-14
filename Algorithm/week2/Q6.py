# 문제 : 패턴 압축

string_item = list(input())
string_len = len(string_item)

zip_result = ""

counter = 1
checking_char = string_item[0]

for i in range(string_len-1):
  if string_item[i] == string_item[i+1]:
    counter+=1
  else :
    zip_result = zip_result +checking_char + str(counter)
    counter = 1
    checking_char = string_item[i+1]

zip_result = zip_result + checking_char + str(counter)

print(zip_result)


