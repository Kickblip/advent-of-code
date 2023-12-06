import os

with open(f'{os.getcwd()}/2023/Python/day02/input.txt', 'r') as f:
    data = f.read().splitlines()
    games, valid_ids = {}, []

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
    valid = True

    for set_id, set in game.items():

        if (set['color'] == 'red' and int(set['count']) > 12) or (set['color'] == 'green' and int(set['count']) > 13) or (set['color'] == 'blue' and int(set['count']) > 14):
            # print(f"Set {set_id} in Game {game_id} is invalid")
            valid = False
            break

    if valid:
        valid_ids.append(int(game_id))

print(sum(valid_ids))
