import os
import re

with open(f'{os.getcwd()}/2023/Python/day03/input.txt', 'r') as f:
    data = f.read().splitlines()

num_arr = []
parts = []

for line in data:
    num_arr += line.split('.')

num_arr = [num for num in num_arr if num.isnumeric()]

print(f'W:{len(data[0])} H:{len(data)}')


def find_numbers_touching_range(s, row_index, start_index, end_index):
    # find all numbers in the string
    numbers = re.finditer(r'\d+', s)
    touching_numbers = []

    for num in numbers:
        # get the start and end index of the current number
        start, end = num.span()

        # check if the number is touching the specified range
        if start <= end_index and end >= start_index + 1:
            touching_numbers.append([row_index, start, end])

    return touching_numbers


for idx, line in enumerate(data):
    for char_idx, char in enumerate(line):
        if not char.isnumeric() and char not in '.' and char in '*':  # character is a gear
            symbol_idx = char_idx

            # check current row
            current_row_nums = find_numbers_touching_range(
                line, idx, symbol_idx - 1, symbol_idx + 1)

            # check row above
            above_row_nums = find_numbers_touching_range(
                data[idx-1], idx-1, symbol_idx - 1, symbol_idx + 1) if idx > 0 else []

            # check row below
            below_row_nums = find_numbers_touching_range(
                data[idx+1], idx+1, symbol_idx - 1, symbol_idx + 1) if idx < len(data) - 1 else []

            numbers = []

            if len(current_row_nums + above_row_nums + below_row_nums) == 2:
                [numbers.append(x) for x in current_row_nums]
                [numbers.append(x) for x in above_row_nums]
                [numbers.append(x) for x in below_row_nums]

                gear = []

                for x in numbers:
                    number = data[x[0]][x[1]:x[2]]

                    gear.append(int(number))

                print(gear)

                gear_ratio = gear[0] * gear[-1]

                parts.append(gear_ratio)

print(sum(parts))
