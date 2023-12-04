import os

with open(f'{os.getcwd()}/day04/input.txt', 'r') as f:
    data = f.read().splitlines()

nums, winning_nums = [], []

for line in data:

    f = line.split('|')

    right = f[-1].split(' ')
    right = [num for num in right if num]

    left = f[0].split(':')[-1].split(" ")
    left = [num for num in left if num]

    nums.append(right)
    winning_nums.append(left)

total = 0

for idx, card in enumerate(nums):
    score = 0
    for x in card:
        if x in winning_nums[idx]:
            if score == 0:
                score += 1
            else:
                score = score * 2
    total += score

print(total)
