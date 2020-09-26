import math


def find_numbers_way(lines, columns, length_diagonal_stroke):
    win_player = '-'

    numbers_way_on_diagonal = math.floor(min(lines, columns) / (length_diagonal_stroke + 1))
    if math.fabs(lines - columns) % 2 != 0:
        win_player = '+'
    if (lines == 1 and columns == 1):
        win_player = '+'
        return win_player
    elif min(lines, columns) == length_diagonal_stroke + 1:
        win_player = '+'
        return win_player
    elif numbers_way_on_diagonal > 2 and (length_diagonal_stroke + 1) * 2 + 2 <= min(lines, columns):
        return win_player
    elif numbers_way_on_diagonal == 1 and (length_diagonal_stroke + 2) == min(lines, columns):
        if win_player == '+':
            win_player = '-'
        else:
            win_player = '+'
        return win_player
    elif numbers_way_on_diagonal == 2 and (length_diagonal_stroke + 1) * 2 + 2 > min(lines, columns) \
            or numbers_way_on_diagonal == 1 and (length_diagonal_stroke + 2) <= min(lines, columns):
        if win_player == '+':
            win_player = '-'
        else:
            win_player = '+'
    return win_player



def find_best_result():
    number_field, length_diagonal_stroke = input().strip().split(' ')
    for i in range(int(number_field)):
        lines, columns = input().strip().split(' ')
        print(find_numbers_way(int(lines), int(columns), int(length_diagonal_stroke)))



find_best_result()
