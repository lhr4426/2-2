# 문제 : 숫자 뒤집고 소수인지 확인

def reverse(item_len, item_list):
    tmp_list = []
    tmp_item = ""
    for i in range(item_len):
        for j in range(len(item_list[i])):
            tmp_item += str(item_list[i][len(item_list[i]) - 1 - j])

        tmp_list.append(int(tmp_item))
        tmp_item = ""

    return tmp_list


def isPrime(item_len, item_list):

    prime_list = []

    for i in range(item_len):

        for j in range(2, item_list[i]):
            if item_list[i] % j == 0:
                break
            else:
                if j == item_list[i] - 1:
                    prime_list.append(item_list[i])

    return prime_list


item_length = int(input())
item_numbers = input().split()

rev_item = reverse(item_length, item_numbers)
prime_item = isPrime(item_length, rev_item)

print(*prime_item)
