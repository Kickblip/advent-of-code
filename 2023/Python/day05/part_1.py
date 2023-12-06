import os

with open(f'{os.getcwd()}/2023/Python/day05/input.txt', 'r') as f:
    data = f.read().splitlines()

map = {}
recent_cat = ''
categories = []

for line in data:

    if line and not line[0].isnumeric():  # category title
        cat_title = line.split(':')[0]
        recent_cat = cat_title
        categories.append(cat_title)

        map[cat_title] = []

    elif line:  # number map
        map[recent_cat].append([int(x) for x in line.split(' ')])

recent_cat = 'seed-to-soil map'
recent_arr = []
print([seed for seed in map['seeds']][0])


def plot(seed_lst):

    global recent_cat
    global recent_arr

    for seed_array in seed_lst:

        for seed in seed_array:

            for cat_lst in map[recent_cat]:

                if cat_lst[1] <= seed <= cat_lst[1] + (cat_lst[2] - 1):
                    new_seed = cat_lst[0] + (seed - cat_lst[1])
                    seed_array[seed_array.index(seed)] = new_seed

        print(seed_array)
        recent_arr = seed_array

        if categories.index(recent_cat) + 2 > len(categories):
            return
        else:
            recent_cat = categories[categories.index(recent_cat) + 1]

            next = []
            next.append(seed_array)
            plot(next)


plot([seed for seed in map['seeds']])

print(f'Smallest Destination: {min(recent_arr)}')
