import os

with open(f'{os.getcwd()}/2023/Python/day08/input.txt', 'r') as f:
    data = f.read().splitlines()

instructions = [0, data.pop(0)]
data.remove('')

choice_to_index = {line.split(' = ')[0]: idx for idx, line in enumerate(data)}

steps = 0
current_index = 0

while True:
    current_line = data[current_index].split(' = ')
    current_line[1] = current_line[1].split(', ')
    current_line[1][0] = current_line[1][0][1:]
    current_line[1][1] = current_line[1][1][:-1]

    if current_line[0] == 'ZZZ':
        break

    current_char = instructions[1][instructions[0]]
    choice = current_line[1][0] if current_char == "L" else current_line[1][1]

    steps += 1
    # print(f"Current line: {current_line}")
    # print(f"Current choice: {current_char}")
    # print(f"Choice: {choice}")

    # Update the current index based on the choice
    current_index = choice_to_index[choice]
    # print(f'Next line: {data[current_index]}')

    # Update the instruction index and wrap around if necessary
    instructions[0] += 1
    if instructions[0] == len(instructions[1]):
        instructions[0] = 0

print(steps)
