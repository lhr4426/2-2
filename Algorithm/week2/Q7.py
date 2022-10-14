# 문제 : 대소문자 변환 알고리즘

big_alpha = list(range(65, 90 + 1))
small_alpha = list(range(97, 122 + 1))
txt_number = list(range(48, 57 + 1))
txt_special = list(range(33, 47 + 1)) + list(range(58, 64 + 1)) + list(
    range(123, 126 + 1))

string_item = ""

while True:
    print("문자열 입력 : ")
    string_item = list(input())
    string_len = len(string_item)

    for i in range(string_len):
        string_item[i] = ord(string_item[i])

    is_big_alpha = False
    is_small_alpha = False
    is_number = False
    is_special = False

    for i in range(string_len):
        if string_item[i] in big_alpha:
            is_big_alpha = True
        elif string_item[i] in small_alpha:
            is_small_alpha = True
        elif string_item[i] in txt_number:
            is_number = True
        elif string_item[i] in txt_special:
            is_special = True

    if is_big_alpha and is_small_alpha and is_number and is_special:
        break
    else:
        print("다시 입력하세요.")

for i in range(len(string_item)):
    if string_item[i] in big_alpha:
        string_item[i] += 32
    elif string_item[i] in small_alpha:
        string_item[i] -= 32
    string_item[i] = chr(string_item[i])

result = ''.join(map(str, string_item))
print(result)
