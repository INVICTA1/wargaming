# input_data = input().strip().split(' ')
# table_size = int(input_data[0])
# digit = int(input_data[1])
# numbers_digit = 0
# if 1 <= table_size <= 10 ** 5 and 1 <= digit <= 10 ** 9:
#     for i in range(1, table_size + 1):
#         if digit % i == 0 and digit / i <= table_size:
#             numbers_digit += 1
#     print(numbers_digit)


def table_pifagor(input_data):
    input_data = input().strip().split(' ')
    table_size = int(input_data[0])
    digit = int(input_data[1])
    numbers_digit = 0
    if 1 <= table_size <= 10 ** 5 and 1 <= digit <= 10 ** 9:
        for i in range(1, table_size + 1):
            if digit % i == 0 and digit / i <= table_size:
                numbers_digit += 1
        print(numbers_digit)
    return numbers_digit

import timeit
code_to_test ='''
input_data = input().strip().split(' ')
table_size = int(input_data[0])
digit = int(input_data[1])
numbers_digit = 0
if 1 <= table_size <= 10 ** 5 and 1 <= digit <= 10 ** 9:
    for i in range(1, table_size + 1):
        if digit % i == 0 and digit / i <= table_size:
            numbers_digit += 1
    print(numbers_digit)
'''
elapsed_time = timeit.timeit(code_to_test, number=1)
print(elapsed_time)
