import os

with open(f'{os.getcwd()}/2023/Python/day05/input.txt', 'r') as f:
    data = f.read().splitlines()

map = {}
recent_cat = ''
categories = []

for line in data:  # populating map
    if line and not line[0].isnumeric():  # category title
        cat_title = line.split(':')[0]
        recent_cat = cat_title
        categories.append(cat_title)

        map[cat_title] = []

    elif line:  # number map
        map[recent_cat].append([int(x) for x in line.split(' ')])


# creating seed list and formatting the map into intervals
old_seed_list = [seed for seed in map['seeds']][0]
seed_list = []

for idx, seed in enumerate(old_seed_list):  # create intervals for seeds
    if idx % 2 == 0:
        seed_list.append([seed, seed + old_seed_list[idx + 1] - 1])

for cat_title, lst in map.items():  # create intervals for categories
    for idx, row in enumerate(lst):
        lst[idx] = [[row[0], row[0] + (row[2] - 1)],
                    [row[1], row[1] + (row[2] - 1)]]
del map['seeds']  # seeds is stored in the seed_list not in the map

print(map)


# start with a category and compare the seed interval to the category intervals

def compare_seeds_to_cat(seed_list, category):
    # cat_lst is a list of 2 subintervals - idx is the row number in the category
    for idx, cat_lst in enumerate(map[category]):
        # print(idx, cat_lst)
        for seed_interval_lst in seed_list:
            print(seed_interval_lst)


ans = compare_seeds_to_cat(seed_list, 'seed-to-soil map')
