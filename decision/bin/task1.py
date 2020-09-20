def table_pifagor(input_data):
    data = input_data.strip().split(' ')
    table_size = int(data[0])
    digit = int(data[1])
    numbers_digit = 0
    if 1 <= table_size <= 10 ** 5 and 1 <= digit <= 10 ** 9:
        for i in range(1, table_size + 1):
            if digit % i == 0 and digit / i <= table_size:
                numbers_digit += 1
    return numbers_digit


print(table_pifagor(input()))
