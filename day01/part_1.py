import os

with open(f'{os.getcwd()}/day_1/input.txt', 'r') as f:
    data = f.read().splitlines()

    calibration_values = []

    for line in data:

        numbers = []
        for char in line:
            if char.isnumeric():
                numbers.append(char)

        calibration_values.append(int(numbers[0] + numbers[-1]))

    print(sum(calibration_values))
