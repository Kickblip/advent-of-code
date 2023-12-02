import os

with open(f'{os.getcwd()}/day02/input.txt', 'r') as f:
    data = f.read().splitlines()
    games = {}
    powers = {}

for line in data:
    game, sets = line.split(': ')
    game_number = game.split(' ')[1]

    if game_number not in games:
        games[game_number] = {}

    for set_index, set in enumerate(sets.split('; ')):
        for cube_index, cube in enumerate(set.split(', ')):
            count, color = cube.split(' ')

            unique_key = f"{set_index}-{cube_index}"

            games[game_number][unique_key] = {
                'color': color,
                'count': count
            }

    for game_id, game in games.items():

        max_vals = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for set_id, set in game.items():

            if (set['color'] == 'red' and int(set['count']) > max_vals['red']):
                max_vals['red'] = int(set['count'])

            if (set['color'] == 'green' and int(set['count']) > max_vals['green']):
                max_vals['green'] = int(set['count'])

            if (set['color'] == 'blue' and int(set['count']) > max_vals['blue']):
                max_vals['blue'] = int(set['count'])

        power = max_vals['red'] * max_vals['green'] * max_vals['blue']

        powers[game_id] = power


print(sum(powers.values()))
