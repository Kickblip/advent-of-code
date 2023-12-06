import os

with open(f'{os.getcwd()}/2023/Python/day01/input.txt', 'r') as f:
    data = f.read().splitlines()

    calibration_values = []

    for line in data:
        numbers = [char for char in line if char.isnumeric()]
        calibration_values.append(int(numbers[0] + numbers[-1]))

    print(sum(calibration_values))
