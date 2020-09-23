def input_data():
    money = int(input('Enter gold: '))
    mass_list = input('Enter 9 integers: ').strip().split(' ')
    return money, mass_list


def create_dict(mass_list):
    dict_digit = {}
    for i in range(1, len(mass_list) + 1):
        dict_digit.update({i: int(mass_list[i - 1])})
    return dict_digit


def find_min_digit(mass_dict, money):
    min_price_digit = 10 ** 6
    min_digit = 0

    for digit, price in mass_dict.items():
        if price < min_price_digit:
            min_price_digit = price
            min_digit = digit

    if min_price_digit > money:
        return 1
    else:
        return (min_price_digit, min_digit)


def add_min_digit_in_list(money, min_price_digit, min_digit):
    list_digit = []
    while money >= min_price_digit:
        money -= min_price_digit
        list_digit.append(min_digit)
    return list_digit, money


def create_list_with_max_digits(dict_digit, min_price_digit, min_digit, money, list_digit):
    for i in range(len(list_digit)):
        newmin_price_digit = min_price_digit
        for price, value in dict_digit.items():
            if price > list_digit[i] and money + newmin_price_digit >= value:
                list_digit[i] = price
                money = money + newmin_price_digit - value
                newmin_price_digit = value
    return list_digit


def create_max_digit(list_digit):
    if type(list_digit) == list:
        list_digit = sorted(list_digit, reverse=True)
        max_digit = 0
        for i in list_digit:
            max_digit = max_digit * 10 + i
        return max_digit
    else:
        return 1


def tactical_number(money_and_mass_list):
    print(money_and_mass_list)
    money, mass_list = money_and_mass_list
    dict_digit = create_dict(mass_list)

    min_price_and_digit = find_min_digit(dict_digit, money)
    if min_price_and_digit == 1:
        return 1
    else:
        min_price_digit, min_digit = min_price_and_digit
    list_digit, money = add_min_digit_in_list(money, min_price_digit, min_digit)
    list_digit = create_list_with_max_digits(dict_digit, min_price_digit, min_digit, money, list_digit)
    max_number = create_max_digit(list_digit)
    return max_number


print(tactical_number(input_data()))
