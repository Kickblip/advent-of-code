import os

with open(f'{os.getcwd()}/day04/input.txt', 'r') as f:
    data = f.read().splitlines()

nums, winning_nums, count = [], [], []

for line in data:

    f = line.split('|')

    right = f[-1].split(' ')
    right = [num for num in right if num]

    left = f[0].split(':')[-1].split(" ")
    left = [num for num in left if num]

    nums.append(right)
    winning_nums.append(left)

for x in range(0, len(nums)):
    count.append(1)

for idx, card in enumerate(nums):
    amount_winners = 0

    for x in card:
        if x in winning_nums[idx]:
            amount_winners += 1

    for x in range(0, amount_winners):
        count[idx + x + 1] += (1 * count[idx])

print(sum(count))
