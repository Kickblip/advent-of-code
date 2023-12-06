import os

with open(f'{os.getcwd()}/day01/input.txt', 'r') as f:
    data = f.read().splitlines()

    calibration_values = []

    number_words = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    for line in data:

        # print(f'line: {line}')
        numbers = []
        buffer = ""
        i = 0
        while i < len(line):
            if line[i].isnumeric():
                numbers.append(line[i])
                i += 1
                continue
            else:
                buffer += line[i]
            for key in number_words.keys():
                if key in buffer:
                    numbers.append(number_words[key])
                    buffer = ""
                    i -= 1
                    break
            i += 1

        # print(f'numbers: {numbers}')
        # print(f"calibration value: {int(numbers[0] + numbers[-1])}")
        calibration_values.append(int(numbers[0] + numbers[-1]))

    # print(calibration_values)
    print(sum(calibration_values))


# 54087
